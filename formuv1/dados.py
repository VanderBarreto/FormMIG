#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 09:53:38 2020

@author: vanderneto
"""


import os
import xml.etree.ElementTree as etree
 

class Dados:
    
    def __init__(self):

        self._lista_metadados = []
        

    def buscar(self,id_revista,end_dspace):
        
        lista_metadados =[]
        print("ID DA REVISTA"+str(id_revista))
        
        if str(id_revista) != "":
        
            ComandoURL = "curl -s -H 'accept: application/xml' "+end_dspace+str(id_revista)+"/metadata"
            print(ComandoURL)
            retorno = os.popen(ComandoURL).read()
            
            root = etree.fromstring(retorno)
            
            for i, campo in enumerate(root):
                
                for j, metadado in enumerate(campo): 
                    if metadado.tag == 'key':
                        meta = metadado.text
                    if metadado.tag == 'value':
                        value = metadado.text
                    
                lista_metadados.append([meta,value])

        self._lista_metadados = lista_metadados
        #print(lista_metadados)
    
    def retorno(self,meta):
        
        saida=""
        
        for i,linha in enumerate(self._lista_metadados):
            if linha[0] == str(meta):
                saida = linha[1]
                
        if str(saida)== "":
            saida = ""
           
        return saida   

        
        
    
    