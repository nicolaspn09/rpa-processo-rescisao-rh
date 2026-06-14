import os
import sys
import time
import random
import psutil
import locale
import smtplib
import psycopg2
import requests
import subprocess
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sys.path.append(r"C:\rpa\Python")

from Classes.Firefox.Firefox.conectaFirefox import FirefoxSeleniumManager


# Envia e-mails
def envia_email(mensagemEmail, destinatarios_email, assunto_email, destinatarios_copia_oculta=None):
    pass # Logica de negocio removida por seguranca corporativa

def handle_exception(bloco_codigo, e):
    pass # Logica de negocio removida por seguranca corporativa

def conecta_pg(sql):
    pass # Logica de negocio removida por seguranca corporativa

def conecta_pg_insert(sql):
    pass # Logica de negocio removida por seguranca corporativa

def find_chrome_processes(ppid):
    pass # Logica de negocio removida por seguranca corporativa

def kill_firefox():
    pass # Logica de negocio removida por seguranca corporativa

def kill_process(pid):
    pass # Logica de negocio removida por seguranca corporativa

def gerar_numero_aleatorio():
    pass # Logica de negocio removida por seguranca corporativa

def dispara_email(nome, matricula, empresa, email, id):
    pass # Logica de negocio removida por seguranca corporativa

def dispara_email_sem_COMPANY_NAME(nome, matricula, empresa, email, id):
    pass # Logica de negocio removida por seguranca corporativa

def dispara_email_sem_usuario(nome, matricula, empresa, email, id):
    pass # Logica de negocio removida por seguranca corporativa

def acessa_navegador():
    pass # Logica de negocio removida por seguranca corporativa

def loga_sistema_intranet():
    pass # Logica de negocio removida por seguranca corporativa

def acessa_tela_cadastro(navegador):
    pass # Logica de negocio removida por seguranca corporativa

def pesquisa_usuario(navegador, usuario):
    pass # Logica de negocio removida por seguranca corporativa

def inativa_usuario(navegador, data_atual):
    pass # Logica de negocio removida por seguranca corporativa

def consulta_inativacao():
    pass # Logica de negocio removida por seguranca corporativa

if __name__ == "__main__":
    consulta_inativacao()