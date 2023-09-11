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
        sleep(1010000010)

    def raspagem_de_dados(self):
        self.contador = 1
        while True:
            self.site_map = {
        'cripto':{
            'name': f"/html/body/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr[{self.contador}]/td[3]/div/a/div/div/p",
            'priece': f"/html/body/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr[{self.contador}]/td[4]/div/a/span",
            'porcentagem1': f"/html/body/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr[{self.contador}]/td[5]/span",
            'porcentagem2': f"/html/body/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr[{self.contador}]/td[6]/span",
            'porcentagem3': f"/html/body/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr[{self.contador}]/td[7]/span",
            'market_cap': f"/html/body/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr[{self.contador}]/td[8]/p/span[2]",
            'volume24h': f"/html/body/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr[{self.contador}]/td[9]/div/a/p",
            'circulating_supply': f"/html/body/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr[{self.contador}]/td[10]/div/div/p",
            'next': f"/html/body/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[6]/div[1]/div/ul/li[10]"
            
        }
        }
            raspan = self.driver.find_element(By.XPATH,self.site_map['cripto']['name']).text
            raspap = self.driver.find_element(By.XPATH,self.site_map['cripto']['priece']).text
            raspaporc1 = self.driver.find_element(By.XPATH,self.site_map['cripto']['porcentagem1']).text
            raspaporc2 = self.driver.find_element(By.XPATH,self.site_map['cripto']['porcentagem2']).text
            raspaporc3 = self.driver.find_element(By.XPATH,self.site_map['cripto']['porcentagem3']).text
            raspamktc = self.driver.find_element(By.XPATH,self.site_map['cripto']['market_cap']).text
            raspavol24 = self.driver.find_element(By.XPATH,self.site_map['cripto']['volume24h']).text
            raspacrcs = self.driver.find_element(By.XPATH,self.site_map['cripto']['circulating_supply']).text


            print(raspan,raspap,raspaporc1,raspaporc2,raspaporc3,raspamktc,raspavol24,raspacrcs)
            self.contador += 1 
            actions = ActionChains(self.driver)
            #solução que encontrei para tecnica de lazy upload da pagina
            actions.send_keys(Keys.PAGE_DOWN).perform()
            actions.send_keys(Keys.END).perform()
        
            print(self.contador)
            if self.contador == 10:
                sleep(4)
                if not self.elemento_xpath_existe(f"/html/body/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[6]/div[1]/div/ul/li[10]"):
                    try:
                        botao_proximo = self.driver.find_element(By.CSS_SELECTOR,self.site_map['cripto']['next'])
                        botao_proximo.click()
                        sleep(4)
                        print('navegando para proxima pagina!!!')
                        self.contador = 1
                        sleep(2)
                    except:
                        print('nao ah mais  paginas!')
                        break


      
    def elemento_xpath_existe(self,xpath):
        try:
            self.driver.find_element(By.XPATH, xpath)
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
        



