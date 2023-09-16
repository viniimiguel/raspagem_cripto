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
from selenium.common.exceptions import NoSuchElementException


class Cripto():
    def __init__(self):
        self.site_link = ('https://www.cryptocompare.com/')
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.site_map = {
            'mostra':{
                'most': '/html/body/div[1]/div[4]/div/div[2]/div/div/homepage-tabs-section/div/div/div/div[1]/div/div[3]/a'
            }
        }
    def abre(self):
        self.driver.get(self.site_link)
        sleep(3)
        self.lazy_upload()
        sleep(3)
        self.driver.find_element(By.XPATH,self.site_map['mostra']['most']).click() # clica para mostrar todas as moedas
        
    def main(self):
        self.abre()
        self.raspa_dados()
        sleep(1279)

    def raspa_dados(self):
        sleep(5)
        self.contador = 1
        while True:
            xpaths = {
                'moedas':{
                    'nome': f'/html/body/div[1]/div[4]/div/div/div/coins-list-v2/div/div/table/tbody/tr[{self.contador}]/td[3]/a/h3/span[1]',
                    'preco': f'/html/body/div[1]/div[4]/div/div/div/coins-list-v2/div/div/table/tbody/tr[{self.contador}]/td[4]/div',
                    'total_vol': f'/html/body/div[1]/div[4]/div/div/div/coins-list-v2/div/div/table/tbody/tr[{self.contador}]/td[6]/div',
                    'toptier_vol': f'/html/body/div[1]/div[4]/div/div/div/coins-list-v2/div/div/table/tbody/tr[{self.contador}]/td[7]/div',
                    'next': f'/html/body/div[1]/div[4]/div/div/div/coins-list-v2/div/div/div[2]/div[2]/a',
                    'cancel': f'/html/body/div[5]/div/div/div[1]/h3/button/span'
                }   
                    
            }
            try:
                self.lazy_upload()

                n = self.driver.find_element(By.XPATH, xpaths['moedas']['nome']).text
                p = self.driver.find_element(By.XPATH, xpaths['moedas']['preco']).text
                t1 = self.driver.find_element(By.XPATH, xpaths['moedas']['total_vol']).text
                t2 = self.driver.find_element(By.XPATH, xpaths['moedas']['toptier_vol']).text
                lis = [f'{n}',f'{p}',f'{t1}',f'{t2}']
                print(lis[0],lis[1],lis[2],lis[3])


                sleep(0.5)
                print(self.contador)
                self.contador += 1
            
            except NoSuchElementException:
                try:
                    botao_proximo = self.driver.find_element(By.XPATH, xpaths['moedas']['next'])
                    if botao_proximo:
                        botao_proximo.click()
                        sleep(4)
                        self.driver.find_element(By.XPATH,xpaths['moedas']['cancel'])
                        print('navegando para proxima pagina !!!')
                        self.contador += 1
                except:
                    break

            except Exception as e:
                print(f'error {e}')


    def lazy_upload(self):
        self.driver.execute_script("window.scrollBy(0,800);")
    




cripto = Cripto()
cripto.main()