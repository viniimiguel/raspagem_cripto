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
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys



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
        contador = 1
        while True:
            self.site_map = {
                'xp':{
                    'nome': f'/html/body/div[1]/div/div/div/article/div/div[7]/div/div/div/div/div/div[3]/table/tbody/tr[{contador}]/td[2]/div/a/div/span[1]',
                    'preco': f'/html/body/div[1]/div/div/div/article/div/div[7]/div/div/div/div/div/div[3]/table/tbody/tr[{contador}]/td[3]/span',
                    'change': f'/html/body/div[1]/div/div/div/article/div/div[7]/div/div/div/div/div/div[3]/table/tbody/tr[{contador}]/td[5]/span',
                    'passa': f'/html/body/div[1]/div/div/div/article/div/div[7]/div/div/div/div/div/div[4]/nav/ul/li[18]',
                }
            }
            try:
                nome = self.driver.find_element(By.XPATH,self.site_map['xp']['nome']).text
                preco = self.driver.find_element(By.XPATH,self.site_map['xp']['preco']).text
                change = self.driver.find_element(By.XPATH,self.site_map['xp']['change']).text

                print(nome)
                print(preco)
                print(change)
                contador += 1
                sleep(0.5)

            except NoSuchElementException:
                self.lazy_upload()
                sleep(2)
                try:
                    passa = self.driver.find_element(By.XPATH, self.site_map['xp']['passa'])
                    if passa:
                        passa.click()
                        sleep(3)
                    else:
                        break
                except:
                    print('xpath nao encontrado!!! ')
                    break
                

            except:
                print('houve algo inesperado!!')
                break


    def lazy_upload(self):
        for i in range(0,3):
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.PAGE_DOWN).perform()

    def planilha(self):
        pass

    def envia(self):
        pass


cripto = Cripto()
cripto.main()
