import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import datetime as DT



days_names = ['Mon','Tue','Wed','Thur','Fri','Sat','Sun','Yesterday,','Thu']
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe",options=options)
driver.maximize_window()
driver.get('https://twitter.com')


try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-testid="loginButton"]'))).click()
except:
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="logInSignUpFooter"]'))).click()
    except:
        pass


try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[autocomplete='username']"))).send_keys('cats0charm')
except:
    pass

try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.css-18t94o4.css-1dbjc4n.r-sdzlij.r-1phboty.r-rs99b7.r-ywje51.r-usiww2.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr.r-13qz1uu'))).click()

except:
    pass

try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[data-testid="ocfEnterTextTextInput"]'))).send_keys('cats0charm')

except:
    pass

try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="ocfEnterTextNextButton"]'))).click()
except:
    pass



try:

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="password"]'))).send_keys('00dg1d2*&**&S')
except:
    pass

try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.css-18t94o4.css-1dbjc4n.r-sdzlij.r-1phboty.r-rs99b7.r-19yznuf.r-64el8z.r-1ny4l3l.r-1dye5f7.r-o7ynqc.r-6416eg.r-lrvibr'))).click()
except:
    pass

try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[aria-label="Expand"]'))).click()
except:
    pass

try:
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[data-testid="conversation"]')))[0].click()
except:
    pass

# satrtrun=input("hit enter to run")

time.sleep(3)
previous = -1
new  =0
flag = False
while True:
    new = len(driver.find_elements_by_css_selector('div.css-1dbjc4n.r-16y2uox.r-1h0z5md.r-1jgb5lz.r-1ye8kvj.r-ymttw5.r-hbs49y.r-13qz1uu div[data-testid="cellInnerDiv"]'))
    if previous == new:
        break
    a=1
    for dat in driver.find_elements_by_css_selector('div.css-901oao.r-1bwzh9t.r-37j5jr.r-n6v787.r-16dba41.r-1cwl3u0.r-bcqeeo.r-fdjqy7.r-qvutc0 span.css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0'):
        print(dat.text)
        result_split = dat.text.split(' ')[0]
        if result_split not in days_names:
            if '/' in result_split:
                flag =True
                break
    if flag:
        break

    ActionChains(driver).move_to_element(driver.find_elements_by_css_selector('div.css-1dbjc4n.r-16y2uox.r-1h0z5md.r-1jgb5lz.r-1ye8kvj.r-ymttw5.r-hbs49y.r-13qz1uu div[data-testid="cellInnerDiv"]')[0]).perform()
    previous = new
    time.sleep(1.25)

previous = 0
new  = -1

while True:
    new = len(driver.find_elements_by_css_selector('div.css-1dbjc4n.r-16y2uox.r-1h0z5md.r-1jgb5lz.r-1ye8kvj.r-ymttw5.r-hbs49y.r-13qz1uu div[data-testid="cellInnerDiv"]'))
    if previous == new:
        break

    for post in driver.find_elements_by_css_selector('div.css-1dbjc4n.r-16y2uox.r-1h0z5md.r-1jgb5lz.r-1ye8kvj.r-ymttw5.r-hbs49y.r-13qz1uu div[data-testid="cellInnerDiv"]')[previous:]:
        try:
            time.sleep(1)
            driver.execute_script("return arguments[0].scrollIntoView(true);", post)
            try:
                post.click()
            except:
                driver.find_element_by_css_selector('body').click()
                pass


        except:
            pass
        time.sleep(1)

    previous = new
    time.sleep(1.5)


driver.quit()
