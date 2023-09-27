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
        self.driver = webdriver.Chrome
        self.site_link('https://www.kraken.com/prices?page=1')
        
    def main(self):
        pass

    def abre(self):
        pass

    def raspagem(self):
        pass

    def lazy_upload(self):
        pass

    def planilha(self):
        pass

    def envia(self):
        pass
