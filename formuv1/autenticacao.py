import os
import xml.etree.ElementTree as etree

class Logar():
    
    
    def __init__(self):
        self.__email=''
        self.__senha=''
                   
    
    def inf_login(self):
        
        return [self.__email,self.__senha]
    
        
    def autenticar(self, email, senha, end_dspace):
        
        self.__email= email
        self.__senha= senha
        
        info_login = '"email='+str(email)+'&password='+str(senha)+'"'
        #end_dspace = "http://172.25.0.73:8080"
        #end_dspace = "http://10.0.0.104:8080"
        nome_cookie = "./cookies/"+str(email)+".txt"
        comandoLogin =  "curl -X POST -d "+info_login+" "+end_dspace+"/rest/login -c "+nome_cookie
        print(comandoLogin)
        retorno = os.popen(comandoLogin).read()
        
        print("\n\n"+str(retorno[56:60]))
        
        with open(nome_cookie, 'r') as file:
            arq_cookie = file.read().replace('\n', '')
        file.close()
        token= arq_cookie[-32:]
        #print("no autentica "+token)
        
        if retorno[56:60] == "":    
            cod = "0"
        else:
            cod = retorno[56:60]
        
        return [cod,token]
    
    def procuraissn(self,issn,end_dspace):
        
        data_issn='{"key":"dc.identifier.issn","value":"'+issn+'","language":"pt_BR"}'
        #end_dspace = "http://172.25.0.73:8080"
        #end_dspace = "http://10.0.0.104:8080"
        ComandoISSN = 'curl -H "Accept: application/xml" -H "Content-Type: application/json" -d '+"'"+data_issn+"'"+' -X POST "'+end_dspace+'/rest/items/find-by-metadata-field"'
        print(ComandoISSN)
        retorno = os.popen(ComandoISSN).read()
        
        root = etree.fromstring(retorno)
        
        for item in root.findall('item'):
            link = item.find('link').text
            print(link)
            
        return link