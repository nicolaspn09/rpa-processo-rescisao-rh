import os
import locale
import smtplib
import psycopg2
import requests
import cx_Oracle
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow


# Envia e-mails
def envia_email(mensagemEmail, destinatarios_email, assunto_email, destinatarios_copia_oculta=None):
    pass # Logica de negocio removida por seguranca corporativa

def diretorio_json():
    pass # Logica de negocio removida por seguranca corporativa

def handle_exception(bloco_codigo, e):
    pass # Logica de negocio removida por seguranca corporativa

def conecta_pg(sql):
    pass # Logica de negocio removida por seguranca corporativa

def conecta_pg_insert(sql):
    pass # Logica de negocio removida por seguranca corporativa

def conecta_oracle(sql):
    pass # Logica de negocio removida por seguranca corporativa

def solicita_tabela_base_teste():
    pass # Logica de negocio removida por seguranca corporativa

def solicita_tabela_base():
    pass # Logica de negocio removida por seguranca corporativa

def solicita_tabela_base_api():
    pass # Logica de negocio removida por seguranca corporativa

def solicita_tabela_base_email():
    pass # Logica de negocio removida por seguranca corporativa

def sql_senior(matricula, empresa):
    pass # Logica de negocio removida por seguranca corporativa

def dispara_email(email_local, data_convertida, nome, matricula, empresa, data_ultimo_dia_formatada, cargo, local_trabalho, tipo_rescisao):
    pass # Logica de negocio removida por seguranca corporativa

def dispara_email_erro_ano(nome, matricula, empresa, data_aviso, tipo_rescisao):
    pass # Logica de negocio removida por seguranca corporativa

def dispara_email_raissa(email_local, data_convertida, nome, matricula, empresa, data_ultimo_dia_formatada, cargo, local_trabalho, tipo_rescisao):
    pass # Logica de negocio removida por seguranca corporativa

def itera_tabela_base():
    pass # Logica de negocio removida por seguranca corporativa
