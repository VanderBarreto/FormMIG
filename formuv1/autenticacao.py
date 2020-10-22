#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 16:31:06 2020

@author: vanderneto
"""

import os
import xml.etree.ElementTree as etree

class Logar():
    
    
    def __init__(self):
        self.__email=''
        self.__senha=''
                   
    
    def inf_login(self):
        
        #if email == None and senha == None:
        #    print(sem informação, retorno valor guardado)
        #    
        #else 
        #    saida=
        
        return [self.__email,self.__senha]
    
        
    def autenticar(self, email, senha):
        
        self.__email= email
        self.__senha= senha
        
        info_login = '"email='+str(email)+'&password='+str(senha)+'"'
        end_dspace = 'http://192.168.10.21:8080'
        nome_cookie = "./cookies/"+str(email)+".txt"
        comandoLogin =  "curl -X POST -d "+info_login+" "+end_dspace+"/rest/login -c "+nome_cookie
        retorno = os.popen(comandoLogin).read()
        
        print("\n\n"+str(retorno[56:60]))
        
        with open(nome_cookie, 'r') as file:
            arq_cookie = file.read().replace('\n', '')
        file.close()
        token= arq_cookie[-32:]
        print("no autentica "+token)
#        retornoo = subprocess.Popen(comandoLogin, stdout=subprocess.PIPE , shell=True )
#        ret = subprocess.check_output(comandoLogin , shell=True)
#        (out, err) = retornoo.communicate()
        
        #comandoConfirma = "curl -H 'Accept: application/json' "+end_dspace+"/status -b cookies.txt"
        
        if retorno[56:60] == "":    
            cod = "0"
        else:
            cod = retorno[56:60]
        
        return [cod,token]
    
    def procuraissn(self,issn):
        
        
        #issn="1678-6408"
        data_issn='{"key":"dc.identifier.issn","value":"'+issn+'","language":"pt_BR"}'
        
        
        retorno = os.popen('curl -H "Accept: application/xml" -H "Content-Type: application/json" -d '+"'"+data_issn+"'"+' -X POST "http://192.168.10.21:8080/rest/items/find-by-metadata-field"').read()
        
        root = etree.fromstring(retorno)
        
        for item in root.findall('item'):
            link = item.find('link').text
            print(link)
            
        return link
        
        #comandoConfirma = "curl -H 'Accept: application/json' "+end_dspace+"/status -b cookies.txt"