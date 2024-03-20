import requests,json,os,random,re
import time as tm
from datetime import datetime
from selenium import webdriver
# from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC ,wait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import self as self
from tkinter import filedialog
from tkinter import *
import tkinter as tk
import pyautogui




# def  intializing_browser():
global driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument('--incognito')
driver = webdriver.Chrome(executable_path="chromedriver.exe", options=chrome_options)

driver.maximize_window()

posts=[]
params = {
    'include_profile_interstitial_type': '1',
    'include_blocking': '1',
    'include_blocked_by': '1',
    'include_followed_by': '1',
    'include_want_retweets': '1',
    'include_mute_edge': '1',
    'include_can_dm': '1',
    'include_can_media_tag': '1',
    'include_ext_has_nft_avatar': '1',
    'skip_status': '1',
    'cards_platform': 'Web-12',
    'include_cards': '1',
    'include_ext_alt_text': 'true',
    'include_quote_count': 'true',
    'include_reply_count': '1',
    'tweet_mode': 'extended',
    'include_ext_collab_control': 'true',
    'dm_users': 'false',
    'include_groups': 'true',
    'include_inbox_timelines': 'true',
    'include_ext_media_color': 'true',
    'supports_reactions': 'true',
    'nsfw_filtering_enabled': 'false',
    'filter_low_quality': 'true',
    'include_quality': 'all',
    'include_ext_edit_control': 'true',
    'ext': 'mediaColor,altText,mediaStats,highlightedLabel,hasNftAvatar,voiceInfo,enrichments,superFollowMetadata,unmentionInfo,editControl,collab_control,vibe',
}

# if u have multiple group put ids here  
# group= ["1541032365027635200",]

# class refreshLogout(Thread):
#     def refreshlog(self):
#         print('thread')
#         rfrshurl=str(driver.current_url)
#         if(rfrshurl=='https://twitter.com/logout/error'):
#             print('Browser refresh')
#             driver.get('https://twitter.com/')
#             tm.sleep(3)
#
#
# while True:
# eror1sol = refreshLogout()
# eror1sol.start()
try:
    f = open('report.txt', 'x')
except:
    try:
        os.remove("report.txt")
        f = open('report.txt', 'x')
    except:
        print('remove if report.txt there')
# def getheader():
#     try:
#         all_jsons = [v for v in driver.requests if 'https://twitter.com/i/api/1.1/dm/conversation/' in v.url]
#         headers = all_jsons[0].headers
#         return headers
#     except Exception:
#         return getheader()
def getheader():
    global headers
    cookies_lst=driver.get_cookies()
    cookies=""
    for i in cookies_lst:
      cookies=cookies+i["name"]+"="+i["value"]+";"
      if i["name"]=="ct0":
        csrf=i["value"]
    js_url="https://abs.twimg.com/responsive-web/client-web/main.f906e9b8.js"
    regex = r"(\"AAAAAAAAAAAAAAAAAAAAA)+(.*?)+(\")"
    bareer = re.search(regex, requests.get(js_url).text).group().replace('"','')
    headers = {'authority': 'api.twitter.com','accept': '*/*',
      'accept-language': 'en-US,en;q=0.9,hi;q=0.8',
      'authorization': 'Bearer '+bareer,
      'cookie': cookies,
      'dnt': '1','origin': 'https://twitter.com','referer': 'https://twitter.com/',
      'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
      'sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site',
      'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36',
      'x-csrf-token': csrf,
      'x-twitter-active-user': 'yes','x-twitter-auth-type': 'OAuth2Session','x-twitter-client-language': 'en'}
    return headers

def extract_list(post_list):
  now= tm.time()
  global last_id,time
  for post in post_list:
      # print(json.dumps(post),'\n \n \n')
      try:
        if post["message"]["conversation_id"] == group_id:
          if post_list.index(post)==0:
            last_id=post["message"]["message_data"]["id"]
            print(last_id,'loading chat........')
          time= post["message"]["time"][:-3]
          if now- int(time) < retwt_within_hrs*3600:
            urls=post["message"]["message_data"]["entities"]["urls"]
            # expanded_url=post["message"]["message_data"]["attachment"]["tweet"]["expanded_url"]
            data= {"time":time,"urls":urls}
            posts.append(data)

      except:
            pass



def get_after_last(last_id):
  print('getting next')
  url = "https://twitter.com/i/api/1.1/dm/conversation/"+group_id+".json?include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1&include_can_dm=1&include_can_media_tag=1&include_ext_has_nft_avatar=1&skip_status=1&cards_platform=Web-12&include_cards=1&include_ext_alt_text=true&include_quote_count=true&include_reply_count=1&tweet_mode=extended&include_ext_collab_control=true&dm_users=false&include_groups=true&include_inbox_timelines=true&include_ext_media_color=true&supports_reactions=true&include_conversation_info=true&max_id="+last_id+"&context=FETCH_DM_CONVERSATION_HISTORY&ext=mediaColor%2CaltText%2CmediaStats%2ChighlightedLabel%2ChasNftAvatar%2CvoiceInfo%2Cenrichments%2CsuperFollowMetadata%2CunmentionInfo%2CeditControl%2Ccollab_control%2Cvibe"
  response = requests.request("GET", url, headers=headers)
  data=response.json()["conversation_timeline"]["entries"]
  extract_list(data)

def scrap_start():
  response = requests.get('https://twitter.com/i/api/1.1/dm/inbox_initial_state.json', params=params,  headers=headers)
  data=response.json()["inbox_initial_state"]["entries"]
  # print(json.dumps(data))
  lst=[]
  for i in data:
    try:
        if i["message"]["conversation_id"] == group_id:
          lst.append(i)
    except:
        pass
  extract_list(lst)
  # while tm.time()- int(time) < retwt_within_hrs*3600:
  while TRUE:
    tdif=tm.time() - int(time)
    usertimegiven= retwt_within_hrs * 3600
    if tdif > usertimegiven :
      print('breaking loop')
      break
    get_after_last(last_id)



def filter():
  def slst(elmnt):
    d=dict(elmnt)
    return d["time"]
  posts.sort(key=slst)
  f_posts=[]
  for i in posts:
    # f_posts.append(i["url"])
    try:
      for u in i["urls"]:
        try:
          u1=(u["expanded_url"])
          if "twitter.com/" in u1:
            f_posts.append(u1)
        except:
            pass
    except:
      pass
  final_list=[]
  [final_list.append(i) for i in f_posts if i not in final_list]
  return final_list

def Account_login():
    global cookie
    # tweetUSer = os.environ['tweetUSer']
    tweetUSer = uservalue.get()
    # tweetPass = os.environ['tweetPas']
    tweetPass = passvalue.get()
    driver.get("https://twitter.com/login")
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//input[@name='text']"))).send_keys(tweetUSer)
    tm.sleep(random.uniform(1, 2))
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//input[@name='text']"))).send_keys(Keys.ENTER)
    tm.sleep(random.uniform(1, 3))
    WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,"//input[@name='password']"))).send_keys(tweetPass)
    tm.sleep(random.uniform(2, 3))
    WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,"//input[@name='password']"))).send_keys(Keys.ENTER)
    tm.sleep(random.uniform(1, 3))
    print('loging account.....')
    getheader()

def clickRTs():
    tm.sleep(4)
    try:
        driver.find_element_by_css_selector('a[data-testid="login"]')
        print('refreshing due to log eror')
        driver.refresh()
    except:
        pass
        tm.sleep(2)
    tm.sleep(3)
    if not driver.find_elements_by_css_selector('div[data-testid="unretweet"]'):
        tm.sleep(3)
        Rt = driver.find_elements_by_css_selector('div[data-testid="retweet"]')
        Rt[0].click()
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-testid='retweetConfirm']"))).click()
        print('Retweeting')
    else:
        print("allready retweeted")
# firstUrl=0

def retweet(url):
  mint1= mintimepuase.get()
  maxt2= maxtimepasue.get()
  driver.get(url)
  tm.sleep(random.uniform(5, 9))
  print(url)
  clickRTs()
  tm.sleep(random.randrange(mint1, maxt2))


List=[]
def main():
  global group_id,retwt_within_hrs
  retwt_within_hrs=rthour.get()
  tm.sleep(5)
  Account_login()
  for i in List:
    group_id=i
    grepo='group id '+ i+'\n'
    f.writelines(grepo)
    print(i)
    scrap_start()
    valid_twt_lst=filter()
    [print(i) for i in valid_twt_lst]
    print(f'total tweets under  {retwt_within_hrs} hour, total valid tweets -> {len(valid_twt_lst)}')
    [retweet(twt) for twt in valid_twt_lst]


# main()
def displayText(path):
    global Counter
    global total_gID
    Counter = 0
    file = open(path, "r")
    # Reading from file
    groupIdlist=file.read()
    CoList = groupIdlist.split("\n")
    for i in CoList:
        if i:
            List.append(i)
            Counter += 1
    sizelist = len(List) - 1
    total_gID=sizelist
    return Counter
def browse_text():
    global textdirect
    # Allow user to select a directory and store it in global var
    # called folder_path

    textdirect = filedialog.askopenfilename(filetypes=(("group", "*.txt"), ("All files", "*")))
    # directory.repalce('/','\')
    folder_p.set(textdirect)
    print("total group",displayText(textdirect))

root = Tk()
root.geometry("1200x500")
root.title("Bot By DaraKhsha_Deepak")
root['background'] = '#8C65D3'

# credential
mintimepuase= IntVar()
maxtimepasue = IntVar()
Label(root, text="UserName", font="Roboto,14,bold", bg="#8C65D3", fg="white").grid(row=0)
Label(root, text="Password", font="Roboto,14,bold", bg="#8C65D3", fg="white").grid(row=1)
Label(root, text="Group id text", font="Roboto,14,bold", bg="#8C65D3", fg="white").grid(row=2)
Label(root, text="how many hours msgs u wanna tweet ?", font="Roboto,14,bold", bg="#8C65D3", fg="white").grid(row=3)
Label(root, text="min time sec", font="Roboto,14,bold", bg="#8C65D3", fg="white").grid(row=4,column=0)
tk.Spinbox(root,from_= 1, to = 99999.0,width=4, increment=10,textvariable=mintimepuase).grid(row=4,column=1)
Label(root, text="max time sec", font="Roboto,14,bold", bg="#8C65D3", fg="white").grid(row=4,column=2)
tk.Spinbox(root,from_= 1, to = 99999.0,width=4, increment=10,textvariable=maxtimepasue).grid(row=4,column=3)

# entry
uservalue = StringVar()
passvalue = StringVar()
rthour=IntVar()
# data
userentry = Entry(root, textvariable=uservalue)
passentry = Entry(root, textvariable=passvalue)
Entry(root, textvariable=rthour).grid(row=3,column=1)

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)
folder_p=StringVar()

lbl2 = Label(master=root, textvariable=folder_p)
lbl2.grid(row=2, column=2)
button3 = Button(text="Browse text", command=browse_text).grid(row=2, column=1)

Button(text="Run Bot", command=main).grid()
root.mainloop()
  


