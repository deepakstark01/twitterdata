import os
import random
from tkinter import *
import tkinter as tk
import sys
from time import sleep
import time
# import pyautogui
import sys
from dateutil import parser
import time
import random
import requests
import json
# import datetime
# import self as self
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import selenium
from seleniumwire import webdriver
from pynput.keyboard import Controller, Key
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC ,wait
from bs4 import BeautifulSoup
from datetime import datetime
from datetime import timedelta
# url = 'https://twitter.com/i/api/1.1/dm/inbox_initial_state.json?include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1&include_can_dm=1&include_can_media_tag=1&include_ext_has_nft_avatar=1&skip_status=1&cards_platform=Web-12&include_cards=1&include_ext_alt_text=true&include_quote_count=true&include_reply_count=1&tweet_mode=extended&include_ext_collab_control=true&dm_users=true&include_groups=true&include_inbox_timelines=true&include_ext_media_color=true&supports_reactions=true&nsfw_filtering_enabled=false&filter_low_quality=true&include_quality=all&include_ext_edit_control=true&ext=mediaColor%2CaltText%2CmediaStats%2ChighlightedLabel%2ChasNftAvatar%2CvoiceInfo%2Cenrichments%2CsuperFollowMetadata%2CunmentionInfo%2CeditControl%2Ccollab_control%2Cvibe'
# url1 = 'https://twitter.com/i/api/1.1/dm/conversation/1541019474782212096.json?include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1&include_can_dm=1&include_can_media_tag=1&include_ext_has_nft_avatar=1&skip_status=1&cards_platform=Web-12&include_cards=1&include_ext_alt_text=true&include_quote_count=true&include_reply_count=1&tweet_mode=extended&include_ext_collab_control=true&dm_users=false&include_groups=true&include_inbox_timelines=true&include_ext_media_color=true&supports_reactions=true&include_conversation_info=true&max_id=1553049286354472965&context=FETCH_DM_CONVERSATION_HISTORY&ext=mediaColor%2CaltText%2CmediaStats%2ChighlightedLabel%2ChasNftAvatar%2CvoiceInfo%2Cenrichments%2CsuperFollowMetadata%2CunmentionInfo%2CeditControl%2Ccollab_control%2Cvibe'
# url2 = 'https://twitter.com/i/api/1.1/dm/conversation/1541019474782212096.json?include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1&include_can_dm=1&include_can_media_tag=1&include_ext_has_nft_avatar=1&skip_status=1&cards_platform=Web-12&include_cards=1&include_ext_alt_text=true&include_quote_count=true&include_reply_count=1&tweet_mode=extended&include_ext_collab_control=true&dm_users=false&include_groups=true&include_inbox_timelines=true&include_ext_media_color=true&supports_reactions=true&include_conversation_info=true&max_id=1554011780128571396&context=FETCH_DM_CONVERSATION_HISTORY&ext=mediaColor%2CaltText%2CmediaStats%2ChighlightedLabel%2ChasNftAvatar%2CvoiceInfo%2Cenrichments%2CsuperFollowMetadata%2CunmentionInfo%2CeditControl%2Ccollab_control%2Cvibe'
f = open('report.txt', 'x')

def run_chrome():
    global driver

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    chrome_options.add_argument('--incognito')
    driver = webdriver.Chrome(executable_path="C:\chromedriver.exe", options=chrome_options)

    print("work")
    url="https://www.twitter.com/login"
    driver.get(url)
def Account_login():
    accountTXt = open("account.txt", 'r')
    dataacc= accountTXt.read()
    logLIst = dataacc.splitlines()
    print(logLIst)
    tweetUSer = logLIst[0]
    tweetPass = logLIst[1]
    run_chrome()
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//input[@name='text']"))).send_keys(tweetUSer)
    time.sleep(random.uniform(1, 2))
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//input[@name='text']"))).send_keys(Keys.ENTER)
    time.sleep(random.uniform(1, 3))
    WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,"//input[@name='password']"))).send_keys(tweetPass)
    time.sleep(random.uniform(2, 3))
    WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,"//input[@name='password']"))).send_keys(Keys.ENTER)
    time.sleep(random.uniform(1, 3))
global userTime
userTime=input("Enter the time in hours : ")
Account_login()
driver.maximize_window()


def mdy_to_ymd(d):
#      return datetime.strptime(d, '%b %d, %Y, %I:%M %p').strftime('%Y-%m-%d %I:%M:%p')
     return datetime.strptime(d, '%Y-%m-%d %I:%M %p').strftime('%Y-%m-%d %I:%M:%p')

def timeLogic(datPost):
#     if('yesterday'in datPost):
#         currntday=UserTweetDays+1
#         return currntday 
#     else:
    #     UserDays = datetime.now() - timedelta(days=UserTweetDays)
    UserDays = datetime.now()
    UserDays = UserDays.strftime("%Y-%m-%d %I:%M:%p")
    print("Current time : ",UserDays)
    UserDays=datetime.strptime(UserDays, '%Y-%m-%d %I:%M:%p')
    dateVal=mdy_to_ymd(datPost)
    print("post Time :",end=" ")
    dateVal=datetime.strptime(dateVal, '%Y-%m-%d %I:%M:%p')
    print(dateVal)
    dayval=UserDays-dateVal
    currntday=int(dayval.seconds//3600)
    print("Hour Gap of post : ",currntday)
    return currntday


def helper():
    days_names = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun', 'Yesterday', 'Thu']

    time.sleep(3)
    previous = -1
    new = 0
    skipT = 0
    getRight = 0
    flag = False
    while True:
        new = len(driver.find_elements_by_css_selector(
            'div.css-1dbjc4n.r-16y2uox.r-1h0z5md.r-1jgb5lz.r-1ye8kvj.r-ymttw5.r-hbs49y.r-13qz1uu div[data-testid="cellInnerDiv"]'))
        if previous == new:
            break
        a = 1
        ourself = 'div.css-901oao.r-1bwzh9t.r-37j5jr.r-n6v787.r-16dba41.r-1cwl3u0.r-bcqeeo.r-1ff274t.r-qvutc0 span.css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0'
        sender = 'div.css-901oao.r-1bwzh9t.r-37j5jr.r-n6v787.r-16dba41.r-1cwl3u0.r-bcqeeo.r-fdjqy7.r-qvutc0>span.css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0:nth-of-type(3)'
        timeList = ourself + sender
        # private =driver.find_elements_by_css_selector('div.css-901oao.r-1bwzh9t.r-37j5jr.r-n6v787.r-16dba41.r-1cwl3u0.r-bcqeeo.r-fdjqy7.r-qvutc0 span.css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0')
        group = driver.find_elements_by_xpath(
            '//*[@id="layers"]/div/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/span[3]')
        # dateData = driver.find_elements_by_css_selector(sender)
        #     dateData=driver.find_elements_by_css_selector(sender)
        for dat in driver.find_elements_by_css_selector(sender):
            print(dat.text)
            if ('Seen' in dat.text):
                continue
            if (len(dat.text) > 9):
                flag = True
                break
            t2 = dat.text
            t = datetime.now().date()
            t = str(t) + " " + t2

            try:
                checkTime = timeLogic(t)
                print(checkTime)

            except Exception:
                print("exception")
                continue
                pass
            if ((checkTime) > int(userTime)):
                print("scrolling above stoped !")
                flag = True
                break
            result_split = dat.text.split(' ')[0]
            #         print(result_split)
            if result_split not in days_names:
                if '/' in result_split:
                    flag = True
                    break

        if flag:
            break

        skip = len(driver.find_elements_by_css_selector(
            'div.css-1dbjc4n.r-16y2uox.r-1h0z5md.r-1jgb5lz.r-1ye8kvj.r-ymttw5.r-hbs49y.r-13qz1uu div[data-testid="cellInnerDiv"]'))
        ActionChains(driver).move_to_element(driver.find_elements_by_css_selector(
            'div.css-1dbjc4n.r-16y2uox.r-1h0z5md.r-1jgb5lz.r-1ye8kvj.r-ymttw5.r-hbs49y.r-13qz1uu div[data-testid="cellInnerDiv"]')[
                                                 skip - 1]).perform()

        previous = new
        time.sleep(1.25)

    previous = 0
    new = -1


def reweetFromGroup():
    days_names = ['Mon','Tue','Wed','Thur','Fri','Sat','Sun','Yesterday','Thu']
    previous = 0

    while True:

        new = len(driver.find_elements_by_css_selector('div.css-1dbjc4n.r-16y2uox.r-1h0z5md.r-1jgb5lz.r-1ye8kvj.r-ymttw5.r-hbs49y.r-13qz1uu div[data-testid="cellInnerDiv"]'))
        if previous == new:
            driver.execute_script("return arguments[0].scrollIntoView(true);", driver.find_elements_by_css_selector('div.css-1dbjc4n.r-16y2uox.r-1h0z5md.r-1jgb5lz.r-1ye8kvj.r-ymttw5.r-hbs49y.r-13qz1uu div[data-testid="cellInnerDiv"]')[0])
            time.sleep(4.5)
            new  = len(driver.find_elements_by_css_selector('div.css-1dbjc4n.r-16y2uox.r-1h0z5md.r-1jgb5lz.r-1ye8kvj.r-ymttw5.r-hbs49y.r-13qz1uu div[data-testid="cellInnerDiv"]'))
            if new == previous:
                break

        driver.execute_script("return arguments[0].scrollIntoView(true);", driver.find_elements_by_css_selector('div.css-1dbjc4n.r-16y2uox.r-1h0z5md.r-1jgb5lz.r-1ye8kvj.r-ymttw5.r-hbs49y.r-13qz1uu div[data-testid="cellInnerDiv"]')[0])
        time.sleep(5)

        previous = new
        # time.sleep(1.5)

    
twitt_urls = []
time.sleep(random.uniform(1, 2))
Gtxt = open("groupData.txt", 'r')
Gdata = Gtxt.read()
listG = Gdata.splitlines()
g=1
for group in listG:
    driver.get(group)
    dataG="Group "+str(g)+": "+group+'\n\n'
    print("Group ",g,": ",group)
    f.writelines(dataG)
    time.sleep(random.uniform(2, 5))
    # reweetFromGroup()
    helper()
    all_jsons = [v for v in driver.requests if 'https://twitter.com/i/api/1.1/dm/conversation/' in v.url]
    for jso in all_jsons:
        headers = jso.headers
        url_json = jso.url
        response_json = json.loads(requests.get(url=url_json,headers=headers).text)

        for enttry in response_json['conversation_timeline']['entries']:
            item = dict()
            try:
                item['expand_url'] = enttry['message']['message_data']['attachment']['tweet']['expanded_url']
                item['date'] = parser.parse(enttry['message']['message_data']['attachment']['tweet']['status']['created_at'])
                twitt_urls.append(item)
            except:
                try:
                    if 'https' in enttry['message']['message_data']['text']:
                        item['expand_url'] = enttry['message']['message_data']['text']
                        item['date'] = ''
                        twitt_urls.append(item)
                        a=1
                except:
                    continue
                    # pass

    today = datetime.now()
    check_url = []
    indexValurl=0
    for n in twitt_urls:
        # if(indexValurl<1):
        #     dataN=n['expand_url']+'\n'
        #     f.writelines(dataN)
        # if(indexValurl==len(twitt_urls-1)):
        #
        #     dataN2=n['expand_url']+'\n'
        #     f.writelines(dataN2)
        try:
            difference = today - n['date'].replace(tzinfo=None)
            print(n['date'])
            if (difference.days > 1) and (n['expand_url'] not in check_url) :
                driver.get(n['expand_url'])
                print(n['expand_url'])
                time.sleep(3)
                check_url.append(n['expand_url'])
                try:
                    # likeCLi = driver.find_element_by_css_selector("div[data-testid='like']")
                    # driver.execute_script("arguments[0].click();", likeCLi)
                    time.sleep(3)
                    Rt = driver.find_element_by_css_selector('div[data-testid="retweet"]')
                    driver.execute_script("arguments[0].click();", Rt)
                except:
                    print("already retweeted")

                a=1

        except:
            if (n['expand_url'] not in check_url):
                driver.get(n['expand_url'])
                time.sleep(3)
                check_url.append(n['expand_url'])
                try:
                    # likeCLi = driver.find_element_by_css_selector("div[data-testid='like']")
                    # driver.execute_script("arguments[0].click();", likeCLi)
                    time.sleep(3)
                    Rt = driver.find_element_by_css_selector('div[data-testid="retweet"]')
                    driver.execute_script("arguments[0].click();", Rt)
                except:
                    print("already retweeted")

        indexValurl+=1
    g+=1
