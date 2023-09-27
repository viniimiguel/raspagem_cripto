from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import openpyxl
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from selenium.common.exceptions import NoSuchElementException



class Cripto():
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()
        self.site_link = ('https://www.kraken.com/prices?page=1')

    def abre(self):
        self.driver.get(self.site_link)
        self.driver.maximize_window()
        
    def main(self):
        self.abre()
        self.raspagem()
        sleep(123123213)

    def raspagem(self):
        self.site_map = {
            'xp':{
                'nome': '/html/body/div[1]/div/div/div/article/div/div[7]/div/div/div/div/div/div[3]/table/tbody/tr[1]/td[2]/div/a/div/span[1]',
                'preco': '/html/body/div[1]/div/div/div/article/div/div[7]/div/div/div/div/div/div[3]/table/tbody/tr[1]/td[3]/span',
                'change': '/html/body/div[1]/div/div/div/article/div/div[7]/div/div/div/div/div/div[3]/table/tbody/tr[1]/td[5]/span',
            }
        }
        while True:
            try:
                nome = self.driver.find_element(By.XPATH,self.site_map['xp']['nome']).text
                preco = self.driver.find_element(By.XPATH,self.site_map['xp']['preco']).text
                change = self.driver.find_element(By.XPATH,self.site_map['xp']['change']).text

                print(nome)
                print(preco)
                print(change)
                
            except NoSuchElementException:
                break

            except:
                pass

    def lazy_upload(self):
        pass

    def planilha(self):
        pass

    def envia(self):
        pass


cripto = Cripto()
cripto.main()
