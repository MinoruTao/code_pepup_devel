###ログインログオフのみ#＃＃
import datetime
import time
import boto3
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def lambda_handler(event,context):

    #pepup関連の変数
    URL="https://pepup.life/users/sign_in"
    username = 'tsae360@gmail.com'
    password = 'passwd'

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument("--disable-application-cache")
    options.add_argument("--disable-infobars")
    options.add_argument("--no-sandbox")
    options.add_argument("--hide-scrollbars")
    options.add_argument("--enable-logging")
    options.add_argument("--log-level=0")
    options.add_argument("--v=99")
    options.add_argument("--single-process")
    options.add_argument("--ignore-certificate-errors")
    # Headless Chromeを起動
    options.binary_location = "./bin/headless-chromium"
    driver = webdriver.Chrome(executable_path="./bin/chromedriver",chrome_options=options)

    driver.get(URL)

    userNameField = driver.find_element_by_id('sender-email')
    userNameField.send_keys(username) 

    passwordField = driver.find_element_by_id('user-pass')
    passwordField.send_keys(password)

    submitButton = driver.find_element_by_name('commit')
    submitButton.click()

    ToDailyInput = driver.find_element_by_class_name('SideMenu_MyFitnessDataIcon')
    ToDailyInput.click()

    tmp = driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[2]/div/div[4]/div[2]/div[*]/label')
    for ch in tmp:
        ch.click()

    driver.back()

    #ログオフ
    TOHOME = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div/div[1]/a/img')
    TOHOME.click()
    LogoffMenuButton = driver.find_element_by_class_name('Header_DropdownLink') 
    LogoffMenuButton.click()
    LogoffButton = driver.find_element_by_class_name('Header_DropdownLogOutIcon') 
    LogoffButton.click()

    driver.quit() 
