"""
@author: vanderneto
"""

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .autenticacao import Logar
from .dados import Dados
from django import forms
import os
import json

g_link=""
form = None
g_token=""

class Revistas:
    
    
    def __init__(self):
        
        print("\n carreguei \n")
    
    def carregar(request,Id):
        
        if Id == 1:
            from .forms import ContactForm
            print("entrei em 1\n")
            form_class = ContactForm            
            return form_class
        
        if Id == 2:
            
            print("entrei em 2\n")
            print(type(form))
            form2 = ContactForm(request)
            print(type(form2))
            return form2
            
    
    def revista(self, request):
        
        global g_link
        global g_token
        global form
        
        submitted = False
        
            
        if request.method == 'POST':
            
            token = g_token
            end_dspace_metadata = "http://172.25.0.73:8080"+g_link+"/metadata"
            
            metadata ='[{"key":"dc.contributor.editor","value":"'+str(request.POST.get('dccontributoreditor'))+'","language":"pt_BR"},{"key":"dc.date.accessioned","value":"'+str(request.POST.get('dcdescriptionabastract'))+'"},{"key":"dc.date.available","value":"'+str(request.POST.get('dcdescriptionabastract'))+'"},{"key":"dc.identifier.issn","value":"'+str(request.POST.get('dcdescriptionabastract'))+'","language":"pt_BR"},{"key":"dc.identifier.uri","value":"'+str(request.POST.get('dcdescriptionabastract'))+'"},{"key":"dc.language","value":"'+str(request.POST.get('dcdescriptionabastract'))+'","language":"pt_BR"},{"key":"dc.title","value":"'+str(request.POST.get('dcdescriptionabastract'))+'","language":"pt_BR"},{"key":"dc.subject.cnpq","value":"'+str(request.POST.get('dcdescriptionabastract'))+'","language":"pt_BR"},{"key":"dc.title.abbreviated","value":"'+str(request.POST.get('dcdescriptionabastract'))+'","language":"pt_BR"},{"key":"dc.title.proper","value":"'+str(request.POST.get('dcdescriptionabastract'))+'","language":"pt_BR"},{"key":"dc.identifier.issnl","value":"'+str(request.POST.get('dcdescriptionabastract'))+'","language":"pt_BR"},{"key":"dc.description.situation","value":"'+str(request.POST.get('dcdescriptionabastract'))+'","language":"pt_BR"},{"key":"dc.date.startyear","value":"'+str(request.POST.get('dcdescriptionabastract'))+'","language":"pt_BR"},{"key":"dc.identifier.url","value":"'+str(request.POST.get('dcdescriptionabastract'))+'","language":"pt_BR"},{"key":"dc.publisher.name","value":"'+str(request.POST.get('dcdescriptionabastract'))+'","language":"pt_BR"},{"key":"dc.publisher.legalnature","value":"'+str(request.POST.get('dcdescriptionabastract'))+'","language":"pt_BR"},{"key":"dc.identifier.email","value":"'+str(request.POST.get('dcdescriptionabastract'))+'","language":"pt_BR",{"key":"dc.description.cep","value":"'+str(request.POST.get('dcdescriptionabastract'))+'","language":"pt_BR"},{"key":"dc.description.state","value":"'+str(request.POST.get('dcdescriptionabastract'))+'","language":"pt_BR"},{"key":"dc.description.neighborhood","value":"'+str(request.POST.get('dcdescriptionabastract'))+'"},{"key":"dc.description.street","value":"'+str(request.POST.get('dcdescriptionabastract'))+'","language":"pt_BR"},{"key":"dc.description.phone","value":"'+str(request.POST.get('dcdescriptionabastract'))+'","language":"pt_BR"},{"key":"dc.description.periodicity","value":"'+str(request.POST.get('dcdescriptionabastract'))+'","language":"pt_BR"},{"key":"dc.rights.preprint","value":"'+str(request.POST.get('dcdescriptionabastract'))+'","language":"pt_BR"},{"key":"dc.rights.authorpostprint","value":"'+str(request.POST.get('dcdescriptionabastract'))+'","language":"pt_BR"},{"key":"dc.rights.journalpostprint","value":"'+str(request.POST.get('dcdescriptionabastract'))+'","language":"pt_BR"},{"key":"dc.rights.sealcolor","value":"'+str(request.POST.get('dcdescriptionabastract'))+'","language":"pt_BR"},{"key":"dc.rights.time","value":"'+str(request.POST.get('dcdescriptionabastract'))+'","language":"pt_BR"},{"key":"dc.rights.access","value":"'+str(request.POST.get('dcdescriptionabastract'))+'","language":"pt_BR"},{"key":"dc.rights.creativecommons","value":"'+str(request.POST.get('dcdescriptionabastract'))+'","language":"pt_BR"},{"key":"dc.relation.informationservices","value":"'+str(request.POST.get('dcdescriptionabastract'))+'","language":"pt_BR"},{"key":"dc.relation.informationservices","value":"'+str(request.POST.get('dcdescriptionabastract'))+'","language":"pt_BR"},{"key":"dc.relation.informationservices","value":"'+str(request.POST.get('dcdescriptionabastract'))+'","language":"pt_BR"},{"key":"dc.relation.informationservices","value":"'+str(request.POST.get('dcdescriptionabastract'))+'","language":"pt_BR"},{"key":"dc.relation.informationservices","value":"'+str(request.POST.get('dcdescriptionabastract'))+'","language":"pt_BR"},{"key":"dc.relation.informationservices","value":"'+str(request.POST.get('dcdescriptionabastract'))+'","language":"pt_BR"},{"key":"dc.description.city","value":"'+str(request.POST.get('dcdescriptionabastract'))+'","language":"pt_BR"}]'
            #print(metadata)
            ComandoURL = 'curl --cookie "JSESSIONID='+token+'" -H "accept: application/json" -H "Content-Type: application/json" -X PUT '+end_dspace_metadata+" -d '"+metadata+"'"
            print(ComandoURL)
            os.system(ComandoURL)
            
            metadata=""
            token=""
            form=None
            return HttpResponseRedirect('../login')
            
#                
        else:
            
            print("\ntoken = "+g_token)
            print("\nlink = "+g_link)
            
            if g_token=="":
                mensagem = ""
                return render(request, 'revista/login.html', {"mensagem": mensagem})
                           
            else:
                print("momento 2")
                form = Revistas.carregar(request,1)
                if 'submitted' in request.GET:
                    submitted = True
        
    
        return render(request, 'revista/revista.html', {'form': form, 'submitted': submitted})


        
class Login:
    
    
    def user_login(self, request):
        
        global g_link
        global g_token 
        
        self.user_global= ""
        self.senha_global= ""
        self.revista_global= ""
        self.link_global= ""
        self.token_global=""
        g_link = ""
        g_token = ""
        Autentica=Logar()
        mensagem = "Atualize sua revista"
        
        
        
        if request.method == 'POST':
            
            self.user_global= request.POST.get('email')
            self.senha_global= request.POST.get('senha')
            self.revista_global= request.POST.get('revista')
            
            
            
            if self.user_global != "" and self.senha_global != "" and self.revista_global != "" :
                
                self.link_global = Autentica.procuraissn(self.revista_global)
                g_link = Autentica.procuraissn(self.revista_global)
                print("\nlink = "+g_link)
                (cod, token) = Autentica.autenticar(self.user_global,self.senha_global)
                self.token_global = token 
                g_token = token
                print(g_token)
                #dados_login = Autentica.inf_login()
                
                if self.link_global != "":
                
                    if cod == "0" :
                        
                        return HttpResponseRedirect('/revista')
                        
    #                    if user.is_active:
    #                        login(request,user)
    #                        return HttpResponseRedirect('/revista')
    #                    else:
    #                        return HttpResponse("Your account was inactive.")
    
                    else:
                        mensagem = "Login Inválido"
                        return render(request, 'revista/login.html', {"mensagem": mensagem})
                else:
                    mensagem = "ISSN incorreto"
                    return render(request, 'revista/login.html', {"mensagem": mensagem})
            else:
                mensagem = "Campos faltando"
                return render(request, 'revista/login.html', {"mensagem": mensagem})
                
        else:
            
            
            return render(request, 'revista/login.html', {})
        
   
    def retornoinfo(self):
        
        global g_link

        print("\n\n Revista = "+g_link)
        retorno = g_link
        
        return retorno