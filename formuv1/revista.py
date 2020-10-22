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
#def carregar():
#    ContactForm()
    

class Revistas:
    
    
    def __init__(self):
        
        print("\n carreguei \n")
#        self.user_global=""
#        self.senha_global=""
#        self.revista_global=""
#        self.link_global=""
#        self.token_global=""
#        self.aqui_global = True
    
    def carregar(request,Id):
        
        global form
        
        if Id == 1:
            from .forms import ContactForm
            print("entrei em 1\n")
            form_class = ContactForm
            print(type(form))
            
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
            
            print('[{"key":"dc.contributor.editor","value":"'+str(request.POST.get('dccontributoreditor'))+'","language":"pt_BR"}]')
            
            token = g_token
            end_dspace_metadata = "http://172.25.0.73:8080"+g_link+"/metadata"
            
            #metadata = '[{"key":"dc.description.abstract","value":"'+str(request.POST.get('dcdescriptionabastract'))+'","language":"pt_BR"},{"key":"dc.title","value":"'+str(request.POST.get('dctitle'))+'","language":null},{"key":"dc.title.abbreviated","value":"'+str(request.POST.get('dctitleabbreviated'))+'","language":null},{"key":"dc.title.proper","value":"'+str(request.POST.get('dctitleproper'))+'","language":"pt_BR"}]'
            
            #print(json.dumps(metadata)) 
            
            
            metadata = '[{"key":"dc.contributor.editor","value":"'+str(request.POST.get('dccontributoreditor'))+'","language":"pt_BR"}]'
            print(metadata)
            ComandoURL = 'curl --cookie "JSESSIONID='+token+'" -H "accept: application/json" -H "Content-Type: application/json" -X PUT '+end_dspace_metadata+" -d '"+metadata+"'"
            print(ComandoURL)
            #os.system(ComandoURL)
            
            metadata=""
            toke=""
            
            
            return HttpResponseRedirect('/revista?submitted=True')
            
#                
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
        #Revistas.carregar(request,1)
        Autentica=Logar()
        mensagem = "Atualize sua revista"
        
        
        
        
        if request.method == 'POST':
            
            self.user_global= request.POST.get('email')
            self.senha_global= request.POST.get('senha')
            self.revista_global= request.POST.get('revista')
            
            
            
            if self.user_global != "" and self.senha_global != "" and self.revista_global != "" :
                
                self.link_global = Autentica.procuraissn(self.revista_global)
                g_link = Autentica.procuraissn(self.revista_global)
                (cod, token) = Autentica.autenticar(self.user_global,self.senha_global)
                self.token_global = token 
                g_token = token
                print(g_token)
                #dados_login = Autentica.inf_login()
                
                if self.link_global != "":
                
                    if cod == "0" :
                        
                        #Revistas.carregar()
                        
                        return HttpResponseRedirect('/revista')
                        
    #                    if user.is_active:
    #                        login(request,user)
    #                        return HttpResponseRedirect('/revista')
    #                    else:
    #                        return HttpResponse("Your account was inactive.")
                    else:
                      
                        return HttpResponse("Invalid login details given")
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