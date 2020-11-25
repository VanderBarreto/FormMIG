#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 11:43:50 2020

@author: vanderneto
"""
import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EnviodoEmail:
    
    
    def __init__(self):
        
        return None
        
        
    def envio(nome_revista):
        
        data_e_hora_atuais = datetime.now()
        data_e_hora = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M")
        html = "Revista "+nome_revista+" atualizada.\n Data: "+data_e_hora
        msgHtml = MIMEText(html, 'html')
        
        # Construção da mensagem
        
        msgRoot = MIMEMultipart('related')
        msgRoot['Subject'] = 'Confirmação de Atualização de Revista'
        msgRoot['From'] = 'noreply-oa@ibict.br'
        msgRoot['To'] = ''
        msgRoot.attach(msgHtml)
        
        
        # Configuração SMTP
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("diadorim@ibict.br", "mtasiwhtwlqbblan")

        s.sendmail("diadorim@ibict.br", "diadorim@ibict.br", msgRoot.as_string())
        
        return "email enviado"