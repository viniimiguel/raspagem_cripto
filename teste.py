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
driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[6]/div[1]/div/ul/li[10]').click()

sleep(1201)
