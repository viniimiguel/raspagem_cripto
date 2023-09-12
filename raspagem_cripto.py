#https://coinmarketcap.com/# nome do site que irei fazer a raspagem de dados

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
        self.site_link = 'https://coinmarketcap.com/'
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
   
            
    def main(self):
        self.abre()
        sleep(2)
        self.raspagem_de_dados()
        self.cria_planilhas()

    def raspagem_de_dados(self):
        self.contador = 1
        armazena_nome = ['']
        armazena_preco = ['']
        armazena_porcentagem_1 = ['']
        armazena_porcentagem_2 = ['']
        armazena_porcentagem_3 = ['']
        armazena_market_cap = ['']
        armazena_volume_24h = ['']
        armazena_circulating_supply = ['']
        while True:
            self.site_map = {
        'cripto':{
            'name': f"#__next > div.sc-5909f15e-1.bGBEnA > div.main-content > div.cmc-body-wrapper > div > div:nth-child(1) > div.sc-b28ea1c6-2.kaxzEy > table > tbody > tr:nth-child({self.contador}) > td:nth-child(3) > div > a > div > div > p",
            'priece': f"#__next > div.sc-5909f15e-1.bGBEnA > div.main-content > div.cmc-body-wrapper > div > div:nth-child(1) > div.sc-b28ea1c6-2.kaxzEy > table > tbody > tr:nth-child({self.contador}) > td:nth-child(4) > div > a > span",
            'porcentagem1': f"#__next > div.sc-5909f15e-1.bGBEnA > div.main-content > div.cmc-body-wrapper > div > div:nth-child(1) > div.sc-b28ea1c6-2.kaxzEy > table > tbody > tr:nth-child({self.contador}) > td:nth-child(5) > span",
            'porcentagem2': f"#__next > div.sc-5909f15e-1.bGBEnA > div.main-content > div.cmc-body-wrapper > div > div:nth-child(1) > div.sc-b28ea1c6-2.kaxzEy > table > tbody > tr:nth-child({self.contador}) > td:nth-child(6) > span",
            'porcentagem3': f"#__next > div.sc-5909f15e-1.bGBEnA > div.main-content > div.cmc-body-wrapper > div > div:nth-child(1) > div.sc-b28ea1c6-2.kaxzEy > table > tbody > tr:nth-child({self.contador}) > td:nth-child(7) > span",
            'market_cap': f"#__next > div.sc-5909f15e-1.bGBEnA > div.main-content > div.cmc-body-wrapper > div > div:nth-child(1) > div.sc-b28ea1c6-2.kaxzEy > table > tbody > tr:nth-child({self.contador}) > td:nth-child(8) > p > span.sc-f8982b1f-1.bOsKfy",
            'volume24h': f"#__next > div.sc-5909f15e-1.bGBEnA > div.main-content > div.cmc-body-wrapper > div > div:nth-child(1) > div.sc-b28ea1c6-2.kaxzEy > table > tbody > tr:nth-child({self.contador}) > td:nth-child(9) > div > a > p",
            'circulating_supply': f"#__next > div.sc-5909f15e-1.bGBEnA > div.main-content > div.cmc-body-wrapper > div > div:nth-child(1) > div.sc-b28ea1c6-2.kaxzEy > table > tbody > tr:nth-child({self.contador}) > td:nth-child(10) > div > div.sc-aef7b723-0.sc-e8f714de-1.hSniWt > p",
            'next': "#__next > div.sc-5909f15e-1.bGBEnA > div.main-content > div.cmc-body-wrapper > div > div:nth-child(1) > div.sc-aef7b723-0.sc-e2025c96-0.irGLnh > div.sc-e2025c96-4.knJhpX.hide_for_narrow > div > ul > li.next"
            
        }
        }
            
            try:
                raspan = self.driver.find_element(By.CSS_SELECTOR,self.site_map['cripto']['name']).text
                raspap = self.driver.find_element(By.CSS_SELECTOR,self.site_map['cripto']['priece']).text
                raspaporc1 = self.driver.find_element(By.CSS_SELECTOR,self.site_map['cripto']['porcentagem1']).text
                raspaporc2 = self.driver.find_element(By.CSS_SELECTOR,self.site_map['cripto']['porcentagem2']).text
                raspaporc3 = self.driver.find_element(By.CSS_SELECTOR,self.site_map['cripto']['porcentagem3']).text
                raspamktc = self.driver.find_element(By.CSS_SELECTOR,self.site_map['cripto']['market_cap']).text
                raspavol24 = self.driver.find_element(By.CSS_SELECTOR,self.site_map['cripto']['volume24h']).text
                raspacrcs = self.driver.find_element(By.CSS_SELECTOR,self.site_map['cripto']['circulating_supply']).text

                print(raspan,raspap,raspaporc1,raspaporc2,raspaporc3,raspamktc,raspavol24,raspacrcs)

                armazena_nome.append(raspan)
                armazena_preco.append(raspap)
                armazena_porcentagem_1.append(raspaporc1)
                armazena_porcentagem_2.append(raspaporc2)
                armazena_porcentagem_3.append(raspaporc3)
                armazena_market_cap.append(raspamktc)
                armazena_volume_24h.append(raspavol24)
                armazena_circulating_supply.append(raspacrcs)

                print(self.contador)
                sleep(0.2)
                self.contador += 1
            except:
                self.driver.find_element(By.CSS_SELECTOR,'#__next > div.sc-5909f15e-1.bGBEnA > div.main-content > div.cmc-body-wrapper > div > div:nth-child(1) > div.sc-aef7b723-0.sc-e2025c96-0.irGLnh > div.sc-e2025c96-4.knJhpX.hide_for_narrow > div > ul > li.next').click()
                print('passando para proxima pagina:')
                sleep(4)
                self.contador = 1
                self.lazy_upload()

    def lazy_upload(self):
        for i in range(14):
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.PAGE_DOWN).perform()
        actions.send_keys(Keys.END).perform()

    def cria_planilhas(self,armazena_nome, armazena_preco, armazena_porcentagem_1, armazena_porcentagem_2, armazena_porcentagem_3, armazena_market_cap, armazena_volume_24h, armazena_circulating_supply):
        planilha = openpyxl.Workbook()
        cripto_Moedas = planilha.active
        cripto_Moedas.title = 'Cripto Moedas'
        cripto_Moedas['A1'] = 'Name'
        cripto_Moedas['B1'] = 'Priece'
        cripto_Moedas['C1'] = '1h%'
        cripto_Moedas['D1'] = '24h%'
        cripto_Moedas['E1'] = '7d%'
        cripto_Moedas['F1'] = 'Market Cap'
        cripto_Moedas['G1'] = 'Volume(24h)'
        cripto_Moedas['H1'] = 'Circulating Supply'



        for index, (nome, preco, porcentagem1, porcentagem2, porcentagem3, mcp, vol24, circs) in enumerate(zip(armazena_nome, armazena_preco,armazena_porcentagem_1, armazena_porcentagem_2, armazena_porcentagem_3, armazena_market_cap, armazena_volume_24h, armazena_circulating_supply), start=2):
            cripto_Moedas.crpto(column=1, row=index, value=nome)
            cripto_Moedas.crpto(column=2, row=index, value=preco)
            cripto_Moedas.crpto(column=3, row=index, value=porcentagem1)
            cripto_Moedas.crpto(column=4, row=index, value=porcentagem2)
            cripto_Moedas.crpto(column=5, row=index, value=porcentagem3)
            cripto_Moedas.crpto(column=6, row=index, value=mcp)
            cripto_Moedas.crpto(column=7, row=index, value=vol24)
            cripto_Moedas.crpto(column=8, row=index, value=circs)

        planilha.save('planilha_de_cripto_moedas.xlsx')
        print('Planilha criada com sucesso!')
    def abre(self):
        self.driver.get(self.site_link)
        self.lazy_upload()
        
    



cripto = Cripto()
cripto.main()
        



