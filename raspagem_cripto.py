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


class Cripto():
    def __init__(self):
        self.site_link = ('https://www.cryptocompare.com/')
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
    
    def abre(self):
        self.driver.get(self.site_link)
        sleep(3)
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/div[2]/div/div/homepage-tabs-section/div/div/div/div[1]/div/div[3]/a').click() # clica para mostrar todas as moedas
        
    def main(self):
        self.abre()
        self.raspa_dados()
        sleep(12783971269)

    def raspa_dados(self):
        sleep(10)





cripto = Cripto()
cripto.main()