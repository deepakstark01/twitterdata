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
from selenium.webdriver.common.action_chains import ActionChains
import selenium
from selenium import webdriver
from pynput.keyboard import Controller, Key
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC ,wait
from bs4 import BeautifulSoup

def run_chrome():
    global driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--incognito')
    driver = webdriver.Chrome(executable_path="C:\chromedriver.exe", options=chrome_options)

    print("work")
    url="https://www.twitter.com/login"
    driver.get(url)
    driver.maximize_window()


def Account_login():
    accountTXt = open("account.txt", 'r')
    dataacc = accountTXt.read()
    logLIst = dataacc.splitlines()
    print(logLIst)
    tweetUSer = logLIst[0]
    tweetPass = logLIst[1]
    run_chrome()
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//input[@name='text']"))).send_keys(
        tweetUSer)
    time.sleep(random.uniform(1, 2))
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//input[@name='text']"))).send_keys(
        Keys.ENTER)
    time.sleep(random.uniform(1, 3))
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))).send_keys(
        tweetPass)
    time.sleep(random.uniform(2, 3))
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))).send_keys(
        Keys.ENTER)
    time.sleep(random.uniform(1, 3))

Account_login()


def group():
    time.sleep(random.uniform(1, 2))
    Gtxt = open("groupData.txt", 'r')
    Gdata = Gtxt.read()
    listG = Gdata.splitlines()
    g = 1
    for group in listG:
        driver.get(group)
        print("Group ", g, ": ", group)
        tweetClick()
        time.sleep(random.uniform(2, 5))
        g += 1


def action_scroll():
    pyautogui.click(x=1275, y=829)
    time.sleep(2)
    keyboard = Controller()
    keyboard.press(Key.page_up)
    keyboard.release(Key.page_up)
tweets=driver.find_elements_by_xpath('*//div[@class="css-1dbjc4n r-zmljjp r-vhj8yc r-1867qdf r-rs99b7 r-1loqt21 r-adacv r-1ny4l3l r-1udh08x r-o7ynqc r-6416eg"]')
tweets[0].click()
elment=""
def tweetClick():
    while True:
        time.sleep(2)
        tweets=driver.find_elements_by_xpath('*//div[@class="css-1dbjc4n r-zmljjp r-vhj8yc r-1867qdf r-rs99b7 r-1loqt21 r-adacv r-1ny4l3l r-1udh08x r-o7ynqc r-6416eg"]')
        for i in tweets:
            time.sleep(random.uniform(1, 3))
        #     rtclick = i.find_element_by_xpath('//div//div[@class="css-1dbjc4n r-1awozwy r-18u37iz r-1wbh5a2"]')
        #   rtclick = i.find_element_by_xpath('//a[@href]')
            try:
                driver.execute_script("arguments[0].click();", i)
                time.sleep(random.uniform(2, 3))
            except:
                break
            try:
        #         rt=driver.find_element_by_css_selector('(//div[data-testid="retweet"])[0]')
                rt=driver.find_element_by_css_selector('div[data-testid="retweet"]')
                driver.execute_script("arguments[0].click();", rt)
                time.sleep(random.uniform(2, 3))
                WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Retweet']"))).click()
                time.sleep(random.uniform(1, 3))
            except:
                pass
            time.sleep(random.uniform(3, 6))
            action_scroll()
    #     WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, elment)).send_keys(Keys.PAGE_UP)

        #     WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "(//div[@aria-label='Back'])[2]"))).click()
        #     time.sleep(random.uniform(1, 3))

        #     driver.back()
        #   tweets=driver.find_elements_by_xpath('*//div[@class="css-1dbjc4n r-zmljjp r-vhj8yc r-1867qdf r-rs99b7 r-1loqt21 r-adacv r-1ny4l3l r-1udh08x r-o7ynqc r-6416eg"]')