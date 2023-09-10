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

class Cripto():
    def __init__(self):
        self.site_link = 'https://coinmarketcap.com/'
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.site_map = {
            'cripto':{
                'name': f"/html/body/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr[{self.contador}]/td[3]/div/a/div/div",# /html/body/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr[2]/td[3]/div/a/div/div
                'priece': f"/html/body/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr[{self.contador}]/td[4]/div/a/span",
                'porcentagem1': f"/html/body/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr[{self.contador}]/td[5]/span",
                'porcentagem2': f"/html/body/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr[{self.contador}]/td[6]/span",
                'porcentagem3': f"/html/body/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr[{self.contador}]/td[7]/span",
                'market_cap': f"/html/body/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr[{self.contador}]/td[8]/p/span[2]",
                'volume24h': f"/html/body/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr[{self.contador}]/td[9]/div/a/p",
                'circulating_supply': f"/html/body/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr[{self.contador}]/td[10]/div/div/p",
                
            }
        }
        self.contador = 1
    def main(self):
        self.abre()
        sleep(2)
        self.raspagem_de_dados()
        sleep(1010000010)

    def raspagem_de_dados(self):
     for i in range(len(self.site_map['cripto'])):
        key = list(self.site_map['cripto'].keys())[i]
        value = self.site_map['cripto'][key]
        raspa = self.driver.find_element(By.XPATH, value)
        raspa_txt = raspa.text
        print(raspa_txt)


      
    def elemento_xpath_existe(self, xpath):
        try:
            self.driver.find_element(By.CSS_SELECTOR, xpath)
            return True
        except:
            return False
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
            cripto_Moedas.cpt(column=1, row=index, value=nome)
            cripto_Moedas.cpt(column=2, row=index, value=preco)
            cripto_Moedas.cpt(column=3, row=index, value=porcentagem1)
            cripto_Moedas.cpt(column=4, row=index, value=porcentagem2)
            cripto_Moedas.cpt(column=5, row=index, value=porcentagem3)
            cripto_Moedas.cpt(column=6, row=index, value=mcp)
            cripto_Moedas.cpt(column=7, row=index, value=vol24)
            cripto_Moedas.cpt(column=8, row=index, value=circs)

        planilha.save('planilha_de_cripto_moedas.xlsx')
        print('Planilha criada com sucesso!')
    def abre(self):
        self.driver.get(self.site_link)

cripto =Cripto()
cripto.main()
        



