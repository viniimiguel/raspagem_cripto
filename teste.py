from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import openpyxl
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys



driver = webdriver.Chrome()
driver.get('https://coinmarketcap.com/')
driver.maximize_window()
sleep(3)


sleep(3)
u = driver.find_element(By.CSS_SELECTOR,'#__next > div.sc-82a69b4f-1.hoAtze.global-layout-v2 > div.main-content > div.cmc-body-wrapper > div > div:nth-child(1) > div.sc-b28ea1c6-2.kaxzEy > table > tbody > tr:nth-child(1) > td:nth-child(3) > div > a > div > div > p').text
print(u)
sleep(1201)
