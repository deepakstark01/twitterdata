import os
import random
from tkinter import *
import tkinter as tk
import sys
from time import sleep
import time
import pyautogui
import sys
import time
import random
import self as self
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import selenium
from selenium import webdriver
from pynput.keyboard import Controller, Key
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC ,wait
from bs4 import BeautifulSoup
from datetime import datetime
from datetime import timedelta

reportFile= open('report.txt','w')
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





def reweetFromGroup():
    days_names = ['Mon','Tue','Wed','Thur','Fri','Sat','Sun','Yesterday','Thu']
    userTime=input("Enter the time in hours : ")
    time.sleep(3)
    previous = -1
    new  =0
    skipT=0
    getRight=0
    flag = False
    while True:
        new = len(driver.find_elements_by_css_selector('div.css-1dbjc4n.r-16y2uox.r-1h0z5md.r-1jgb5lz.r-1ye8kvj.r-ymttw5.r-hbs49y.r-13qz1uu div[data-testid="cellInnerDiv"]'))
        if previous == new:
            break
        a=1
        ourself= 'div.css-901oao.r-1bwzh9t.r-37j5jr.r-n6v787.r-16dba41.r-1cwl3u0.r-bcqeeo.r-1ff274t.r-qvutc0 span.css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0'
        sender= 'div.css-901oao.r-1bwzh9t.r-37j5jr.r-n6v787.r-16dba41.r-1cwl3u0.r-bcqeeo.r-fdjqy7.r-qvutc0>span.css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0:nth-of-type(3)'
        timeList=ourself+sender
        #private =driver.find_elements_by_css_selector('div.css-901oao.r-1bwzh9t.r-37j5jr.r-n6v787.r-16dba41.r-1cwl3u0.r-bcqeeo.r-fdjqy7.r-qvutc0 span.css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0')
        group = driver.find_elements_by_xpath('//*[@id="layers"]/div/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/span[3]')
        dateData=driver.find_elements_by_css_selector(sender)
    #     dateData=driver.find_elements_by_css_selector(sender)
        for dat in dateData:
            print(dat.text)
            if('Seen' in dat.text):
                continue
            if(len(dat.text)>9):
                flag =True
                break
            t2=dat.text
            t=datetime.now().date()
            t= str(t)+" "+t2

            try:
                checkTime=timeLogic(t)
                print(checkTime)

            except Exception:
                print("exception")
                continue
                pass
            if((checkTime)>int(userTime)):
                print("scrolling above stoped !")
                flag =True
                break
            result_split = dat.text.split(' ')[0]
    #         print(result_split)
            if result_split not in days_names:
                if '/' in result_split:
                    flag =True
                    break

        if flag:
            break

        skip = len(driver.find_elements_by_css_selector('div.css-1dbjc4n.r-16y2uox.r-1h0z5md.r-1jgb5lz.r-1ye8kvj.r-ymttw5.r-hbs49y.r-13qz1uu div[data-testid="cellInnerDiv"]'))
        ActionChains(driver).move_to_element(driver.find_elements_by_css_selector('div.css-1dbjc4n.r-16y2uox.r-1h0z5md.r-1jgb5lz.r-1ye8kvj.r-ymttw5.r-hbs49y.r-13qz1uu div[data-testid="cellInnerDiv"]')[skip-1]).perform()

        previous = new
        time.sleep(1.25)

    previous = 0
    new  = -1

    while True:

        new = len(driver.find_elements_by_css_selector('div.css-1dbjc4n.r-16y2uox.r-1h0z5md.r-1jgb5lz.r-1ye8kvj.r-ymttw5.r-hbs49y.r-13qz1uu div[data-testid="cellInnerDiv"]'))
        if previous == new:
            break

        pst=0

        for post in driver.find_elements_by_css_selector('div.css-1dbjc4n.r-16y2uox.r-1h0z5md.r-1jgb5lz.r-1ye8kvj.r-ymttw5.r-hbs49y.r-13qz1uu div[data-testid="cellInnerDiv"]')[previous:]:
            try:

                time.sleep(1)
                driver.execute_script("return arguments[0].scrollIntoView(true);", post)
                try:
                    post.click()
                    print(pst," clicked")
                    time.sleep(3)

                    try:
                        pst+=1
                        likeCLi=driver.find_element_by_css_selector("div[data-testid='like']")
                        driver.execute_script("arguments[0].click();",likeCLi)
                        time.sleep(3)
                        Rt=driver.find_element_by_css_selector('div[data-testid="retweet"]')
                        driver.execute_script("arguments[0].click();",Rt)
                        time.sleep(3)
                        driver.find_element_by_css_selector("div[data-testid='retweetConfirm']").click()
                        link=driver.current_url
                        if('photo' in link):
                            # reportFile.writelines(link)
                            print('back')
                            driver.back()
                        else:
                            driver.back()

                            break
                        time.sleep(random.uniform(3, 4))

                    except :
                        print("already retweeted")
                        driver.back()
                        pass
                except:
                    print("except")
                    driver.find_element_by_css_selector('body').click()
                    pass


            except:
                pass
            time.sleep(1)

        previous = new
        time.sleep(1.5)

    

time.sleep(random.uniform(1, 2))
Gtxt = open("groupData.txt", 'r')
Gdata = Gtxt.read()
listG = Gdata.splitlines()
g=1
for group in listG:
    driver.get(group)
    reportFile.writelines(group)
    # print("Group ",g,": ",group)
    time.sleep(random.uniform(2, 5))
    reweetFromGroup()
    g+=1

reportFile.close()
driver.close()