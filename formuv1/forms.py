"""
Created on Tue Jul  7 11:52:27 2020

@author: vanderneto
"""

from django import forms
from .revista import Login
from .dados import Dados


id_revista=""

class DadosRevista:
    
    global id_revista
    
    
    info_login = Login()
    issn_login = info_login.retornoinfo()
    id_revista = issn_login
    


class ContactForm(forms.Form):
    
    global id_revista
    
    print("entrei formulário")
    
    #info_login = Login()
    #id_revista = info_login.retornoinfo()
    print(id_revista)  

    dados_iniciais = Dados()
    dados_iniciais.buscar(id_revista)
    
    op_publicacao = [("Instituição privada","Instituição privada"),("Instituição pública","Instituição pública"),("Organização não governamental(ONG)","Organização não governamental(ONG)"), ("Publicação independente","Publicação independente"), ("Sociedade civil organizada (sindicatos, associações, cooperativas etc.)","Sociedade civil organizada (sindicatos, associações, cooperativas etc.)")]
    
    op_area = [(1,"area1"),(2,"area2")]
    
    
    #Itens
    #Pagina Um
    
    dccontributoreditor = forms.CharField(max_length=200, label='Editor Responsavel', initial = dados_iniciais.retorno('dc.contributor.editor'))
    dcdescriptionabastract = forms.CharField(widget=forms.Textarea,label='Descrição da Revista',initial = dados_iniciais.retorno('dc.description.abstract'))
    dctitle = forms.CharField(max_length=200, label='Titulo',initial = dados_iniciais.retorno('dc.title'))
    dctitleabbreviated = forms.CharField(max_length=100, label='Titulo abreviado',initial = dados_iniciais.retorno('dc.title.abbreviated'))
    dctitleproper = forms.CharField(max_length=100, label='Titulo próprio',initial = dados_iniciais.retorno('dc.title.proper'))
    dctitleother = forms.CharField(max_length=100, label='Outros Títulos',initial = dados_iniciais.retorno('dc.title.other'))
    dctitleprevious = forms.CharField(max_length=100, label='Título anterior',initial = dados_iniciais.retorno('dc.title.previous'))
    dctitlelater = forms.CharField(max_length=100, label='Titulo posterior',initial = dados_iniciais.retorno('dc.title.later'))
    dcidentifierissn = forms.CharField(max_length=100, label='ISSN',initial = dados_iniciais.retorno('dc.identifier.issn'))
    dcidentifierissnl = forms.CharField(max_length=100, label='ISSNL',initial = dados_iniciais.retorno('dc.identifier.issnl'))
    op_dcdescriptionsituation = [("Vigente","Vigente"),("Descontinuada","Descontinuada")]
    dcdescriptionsituation = forms.ChoiceField(choices=op_dcdescriptionsituation,label='Informe a situação da revista',initial = dados_iniciais.retorno('dc.description.situation'))
    dcdatestartyear = forms.DateField(label = 'Informe o ano de publicação',initial = dados_iniciais.retorno('dc.date.startyear'))
    dcdateendyear = forms.DateField(label = 'Ano de finalização de publicação',initial = dados_iniciais.retorno('dc.date.endyear'))
    dcidentifierurl = forms.CharField(max_length=100, label='URL da revista',initial = dados_iniciais.retorno('dc.identifier.url'))
    dcidentifierinteroperabilityprotocol = forms.CharField(max_length=100, label='Protocolo de interoperabilidade', initial = dados_iniciais.retorno('dc.identifier.interoperabilityprotocol'))
    dcidentifierpersistentidentifier = forms.CharField(max_length=100, label='Identificador persistente',initial = dados_iniciais.retorno('dc.identifier.persistentidentifier'))
    op_dclanguages = [("português","português"),("inglês","inglês")]
    dclanguages = forms.ChoiceField(choices=op_dclanguages, label='Idioma',initial = dados_iniciais.retorno('dc.languages'))    

    # Pagina dois
    
    dcsubjectcnpq = forms.ChoiceField(widget=forms.Textarea, label='Area do conhecimento',initial = dados_iniciais.retorno('dc.subject.cnpq'))
    dcpublishername = forms.CharField(max_length=100, label='Instituição editora',initial = dados_iniciais.retorno('dc.publisher.name'))
    dcpublishersubordinate = forms.CharField(max_length=100, label='Organismo subordinado',initial = dados_iniciais.retorno('dc.publisher.subordinate'))
    dcidentifierpublisher = forms.CharField(max_length=100, label='Identificador da instituição editora',initial = dados_iniciais.retorno('dc.identifier.publisher'))
    op_dcpublisherlegalnature = [("Instituição privada","Instituição privada"),\
                                 ("Instituição pública","Instituição pública"),\
                                 ("Organização não governamental(ONG)","Organização não governamental(ONG)"),\
                                 ("Publicação independente","Publicação independente"),\
                                 ("Sociedade civil organizada (sindicatos, associações, cooperativas etc.)","Sociedade civil organizada (sindicatos, associações, cooperativas etc.)")]
    dcpublisherlegalnature = forms.ChoiceField(choices=op_dcpublisherlegalnature, label='Natureza jurídica da instituição editora',initial = dados_iniciais.retorno('dc.publisher.legalnature'))
    dccontributoreditor = forms.CharField(max_length=100, label='Editor responsável',initial = dados_iniciais.retorno('dc.contributor.editor'))
    dcidentifiereditor = forms.CharField(max_length=100, label='Identificador do editor responsável',initial = dados_iniciais.retorno('dc.identifier.editor'))
    dcidentifieremail = forms.EmailField(max_length=100, label='E-mail da revista',initial = dados_iniciais.retorno('dc.identifier.email')) 
    dcdescriptioncep = forms.CharField(max_length=100, label='Código Postal (CEP)',initial = dados_iniciais.retorno('dc.description.cep'))
    op_dcdescriptionstate = [("Acre (AC)","Acre (AC)"),\
                             ("Alagoas (AL)","Alagoas (AL)"),\
                             ("Amapá (AP)","Amapá (AP)")]
    dcdescriptionstate = forms.ChoiceField(choices=op_dcdescriptionstate, label='Estado (UF)', initial = dados_iniciais.retorno('dc.description.state'))
    dcdescriptioncity = forms.CharField(max_length=100, label='Cidade', initial = dados_iniciais.retorno('dc.description.city'))
    dcdescriptionneighborhood = forms.CharField(max_length=100, label='Bairro', initial = dados_iniciais.retorno('dc.description.neighborhood'))
    dcdescriptionstreet = forms.CharField(max_length=100, label='Rua/quadra ou similar', initial = dados_iniciais.retorno('dc.description.street'))
    dcdescriptionbuilding = forms.CharField(max_length=100, label='Casa/Prédio/ Sala ou similar', initial = dados_iniciais.retorno('dc.description.building'))
    dcdescriptionphone = forms.CharField(max_length=100, label='Telefone',initial = dados_iniciais.retorno('dc.description.phone'))
    op_dcdescriptionmodalityofpublication = [("Tradicional","Tradicional"),("Ahead of print","Ahead of print"),("Fluxo contínuo","Fluxo contínuo")]
    dcdescriptionmodalityofpublication = forms.ChoiceField(choices=op_dcdescriptionmodalityofpublication, label='Modalidades de publicação', initial = dados_iniciais.retorno('dc.description.modalityofpublication'))
    
    #Pagina Tres
    
    
    op_dcdescriptionperiodicity = [("Publicação contínua","Publicação contínua"),("Anual","Anual"),("Bianual","Bianual"),("Diária","Diária"),("Mensal","Mensal"),("Quadrienal","Quadrienal"),("Quinquenal","Quinquenal"),("Quinzenal","Quinzenal"),("Semanal","Semanal"),("Semestral","Semestral"),("Trianual","Trianual"),("Trimestral","Trimestral")]
    dcdescriptionperiodicity = forms.ChoiceField(choices=op_dcdescriptionperiodicity, label='Periodicidade de publicação', initial = dados_iniciais.retorno('dc.description.periodicity'))
    op_dcdatemonthofpublication = [("Publicação contínua","Publicação contínua"),("Janeiro","Janeiro"),("Fevereiro","Fevereiro"),("Março","Março"),("Abril","Abril"),("Maio","Maio"),("Junho","Junho"),("Julho","Julho"),("Agosto","Agosto"),("Setembro","Setembro"),("Outubro","Outubro"),("Novembro","Novembro"),("Dezembro","Dezembro")]
    dcdatemonthofpublication = forms.ChoiceField(choices=op_dcdatemonthofpublication, label='Mês de publicação do fascículo', initial = dados_iniciais.retorno('dc.date.monthofpublication'))
    op_period_exp = [("Em branco","Em branco"),("Anual","Anual"),("Bianual","Bianual"),("Diária","Diária"),("Mensal","Mensal"),("Quadrienal","Quadrienal"),("Quinquenal","Quinquenal"),("Quinzenal","Quinzenal"),("Semanal","Semanal"),("Semestral","Semestral"),("Trianual","Trianual"),("Trimestral","Trimestral")]
    dcdescriptioneditorialboardpreiodicity = forms.ChoiceField(choices=op_period_exp, label='Periodicidade de publicação do expediente', initial = dados_iniciais.retorno('dc.description.editorialboardpreiodicity'))
    op_mes_exp = [("Janeiro","Janeiro"),("Fevereiro","Fevereiro"),("Março","Março"),("Abril","Abril"),("Maio","Maio"),("Junho","Junho"),("Julho","Julho"),("Agosto","Agosto"),("Setembro","Setembro"),("Outubro","Outubro"),("Novembro","Novembro"),("Dezembro","Dezembro")]
    dcdateeditorialboardmonthofpublication = forms.ChoiceField(choices=op_mes_exp, label='Mês de publicação do expediente', initial = dados_iniciais.retorno('dc.date.editorialboardmonthofpublication'))
    op_mod_pub_pares = [("Avaliação aberta","Avaliação aberta"),("Avaliação duplo-cego","Avaliação duplo-cego"),("Avaliação simples-cega","Avaliação simples-cega")]
    dcdescriptionpeerreview = forms.ChoiceField(choices=op_mod_pub_pares, label='Modalidade de avaliação por pares', initial = dados_iniciais.retorno('dc.description.peerreview'))
    op_dcdescriptionreviewerspublication= [('A revista publica o nome de avaliadores dos documentos que foram aprovados na avaliação por pares','A revista publica o nome de avaliadores dos documentos que foram aprovados na avaliação por pares'),\
                                           ('A revista publica o nome de todos os avaliadores que participaram da avaliação de documentos por determinado período','A revista publica o nome de todos os avaliadores que participaram da avaliação de documentos por determinado período'),\
                                           ('A revista somente publica avaliadores que concordam com a publicação do seu nome','A revista somente publica avaliadores que concordam com a publicação do seu nome'),\
                                           ('A revista não publica o nome dos avaliadores, mas disponibiliza a lista de pesquisadores cadastrados como possíveis avaliadores','A revista não publica o nome dos avaliadores, mas disponibiliza a lista de pesquisadores cadastrados como possíveis avaliadores'),\
                                           ('A revista não publica, nem revela o nome dos avaliadores','A revista não publica, nem revela o nome dos avaliadores')] 
    dcdescriptionreviewerspublication = forms.ChoiceField(choices=op_dcdescriptionreviewerspublication, label='Publicação dos avaliadores', initial = dados_iniciais.retorno('dc.description.reviewerspublication'))
    op_dcdescriptionreviewerstypeofpublication= [('A revista publica, no expediente, a listagem dos avaliadores que realizaram avaliações','A revista publica, no expediente, a listagem dos avaliadores que realizaram avaliações'),\
                                           ('A revista publica, no corpo do documento aprovado na avaliação por pares, o nome dos avaliadores responsáveis','A revista publica, no corpo do documento aprovado na avaliação por pares, o nome dos avaliadores responsáveis'),\
                                           ('A revista publica os pareceres resultantes das avaliações realizadas com o nome dos avaliadores','A revista publica os pareceres resultantes das avaliações realizadas com o nome dos avaliadores'),\
                                           ('A revista não publica o nome dos avaliadores, mas disponibiliza a lista de pesquisadores cadastrados como possíveis avaliadores','A revista não publica o nome dos avaliadores, mas disponibiliza a lista de pesquisadores cadastrados como possíveis avaliadores'),\
                                           ('A revista não publica, nem revela o nome dos avaliadores','A revista não publica, nem revela o nome dos avaliadores')] 
    dcdescriptionreviewerstypeofpublication = forms.ChoiceField(choices=op_dcdescriptionreviewerstypeofpublication, label='Forma de publicação do nome dos avaliadores', initial = dados_iniciais.retorno('dc.description.reviewerstypeofpublication'))
    op_dcdescriptionreviewersperiodicityofpublication = [("Em branco","Em branco"),("Anual","Anual"),("Bianual","Bianual"),("Diária","Diária"),("Mensal","Mensal"),("Quadrienal","Quadrienal"),("Quinquenal","Quinquenal"),("Quinzenal","Quinzenal"),("Semanal","Semanal"),("Semestral","Semestral"),("Trianual","Trianual"),("Trimestral","Trimestral")]
    dcdescriptionreviewersperiodicityofpublication = forms.ChoiceField(choices=op_dcdescriptionreviewersperiodicityofpublication, label='Periodicidade de publicação do nome dos avaliadores', initial = dados_iniciais.retorno('dc.description.reviewerstypeofpublication'))
    op_dcdescriptionpeerreviewexternality =[("A avaliação por pares é realizada, exclusivamente, por pesquisadores da instituição que edita a revista","A avaliação por pares é realizada, exclusivamente, por pesquisadores da instituição que edita a revista"),\
                                            ("A avaliação por pares é realizada por pesquisadores da instituiçao que edita a revista e por pesquisadores que são externos à instituição que edita a revista","A avaliação por pares é realizada por pesquisadores da instituiçao que edita a revista e por pesquisadores que são externos à instituição que edita a revista"),\
                                            ("A avaliação por pares é realizada, exclusivamente, por pesquisadores que são externos à instituição que edita a revista","A avaliação por pares é realizada, exclusivamente, por pesquisadores que são externos à instituição que edita a revista")]
    dcdescriptionpeerreviewexternality = forms.ChoiceField(choices=op_dcdescriptionpeerreviewexternality, label='Externalidade da avaliação por pares', initial = dados_iniciais.retorno('dc.description.peerreviewexternality'))
    dcdescriptionpeerreviewdocuments = forms.CharField(widget=forms.Textarea, label='Documentos avaliados', initial = dados_iniciais.retorno('dc.description.peerreviewdocuments'))
    dccontributorpublishingresponsable = forms.CharField(max_length=100, label='Responsável pela decisão de publicação', initial = dados_iniciais.retorno('dc.contributor.publishingresponsable'))
    op_dcrightspreprintsubmission = [("A revista aceita a submissão de preprints que já se encontra armazenado em outras plataformas","A revista aceita a submissão de preprints que já se encontra armazenado em outras plataformas"),\
                                     ("A revista não aceita a submissão de preprints que já se encontra armazenado em outras plataformas.","A revista não aceita a submissão de preprints que já se encontra armazenado em outras plataformas")]
    dcrightspreprintsubmission = forms.ChoiceField(choices=op_dcrightspreprintsubmission, label='Permissão de submissão de preprint',initial = dados_iniciais.retorno('dc.rights.preprintsubmission'))
    op_dcrightspreprint = [("A revista permite o armazenamento e acesso, em repositórios institucionais/digitais, da versão preprint do documento submetido para avaliação.","A revista permite o armazenamento e acesso, em repositórios institucionais/digitais, da versão preprint do documento submetido para avaliação."),\
                           ("A revista não permite o armazenamento e acesso, em repositórios institucionais/digitais, da versão preprint do documento submetido para avaliação","A revista não permite o armazenamento e acesso, em repositórios institucionais/digitais, da versão preprint do documento submetido para avaliação")]
    dcrightspreprint = forms.ChoiceField(choices=op_dcrightspreprint, label='Permissão de armazenamento e acesso à versão preprint',initial = dados_iniciais.retorno('dc.rights.preprint'))
    op_dcrightsauthorpostprint = [("A revista permite o armazenamento e acesso, em repositórios institucionais/digitais, da versão pós-print do autor","A revista permite o armazenamento e acesso, em repositórios institucionais/digitais, da versão pós-print do autor"),\
                           ("A revista não permite o armazenamento e acesso, em repositórios institucionais/digitais, da versão pós-print do autor.","A revista não permite o armazenamento e acesso, em repositórios institucionais/digitais, da versão pós-print do autor.")]
    dcrightsauthorpostprint = forms.ChoiceField(choices=op_dcrightsauthorpostprint, label='Permissão de armazenamento e acesso à versão pós-print do autor',initial = dados_iniciais.retorno('dc.rights.authorpostprint'))
    op_dcrightsjournalpostprint = [("A revista permite o armazenamento e acesso, em repositórios institucionais/digitais, da versão pós-print da revista","A revista permite o armazenamento e acesso, em repositórios institucionais/digitais, da versão pós-print da revista"),\
                                   ("A revista não permite o armazenamento e acesso, em repositórios institucionais/digitais, da versão pós-print da revista","A revista não permite o armazenamento e acesso, em repositórios institucionais/digitais, da versão pós-print da revista")]
    dcrightsjournalpostprint = forms.ChoiceField(choices=op_dcrightsjournalpostprint, label='Permissão de armazenamento e acesso à versão pós-prints da revista',initial = dados_iniciais.retorno('dc.rights.journalpostprint'))
    
    
    
    op_dcrightssealcolor = [("Amarela: permite o armazenamento e acesso das versões pré-print dos documentos em repositórios institucionais/digitais","Amarela: permite o armazenamento e acesso das versões pré-print dos documentos em repositórios institucionais/digitais"),\
                            ("Azul: permite o armazenamento e acesso das versões pós-print dos documentos em repositórios institucionais/digitais","Azul: permite o armazenamento e acesso das versões pós-print dos documentos em repositórios institucionais/digitais"),\
                            ("Branca: apresenta restrições para o armazenamento e acesso das versões pré-print e pós-print dos documentos em repositórios institucionais/digitais","Branca: apresenta restrições para o armazenamento e acesso das versões pré-print e pós-print dos documentos em repositórios institucionais/digitais"),\
                            ("Verde: permite o armazenamento e acesso das versões pré-print e pós-print dos documentos em repositórios institucionais/digitais","Verde: permite o armazenamento e acesso das versões pré-print e pós-print dos documentos em repositórios institucionais/digitais")]
    dcrightssealcolor = forms.ChoiceField(choices=op_dcrightssealcolor, label='Selo de armazenamento e acesso',initial = dados_iniciais.retorno('dc.rights.sealcolor'))
    op_dcrightstime = [("Imediatamente após a aceitação do documento","Imediatamente após a aceitação do documento"),\
                       ("Imediatamente após a publicação do documento","Imediatamente após a publicação do documento"),\
                       ("Após finalizado o período de embargo","Após finalizado o período de embargo"),\
                       ("Não permite o armazenamento","Não permite o armazenamento")]
    dcrightstime = forms.ChoiceField(choices=op_dcrightstime, label='Prazo para disponibilização de documentos', initial = dados_iniciais.retorno('dc.rights.time'))
    op_dcrightsaccess = [("Acesso aberto imediato","Acesso aberto imediato"),\
                         ("Acesso aberto após período de embargo","Acesso aberto após período de embargo"),\
                         ("Acesso restrito","Acesso restrito"),\
                         ("Acesso híbrido","Acesso híbrido")]
    dcrightsaccess = forms.ChoiceField(choices=op_dcrightsaccess, label='Tipo de acesso',initial = dados_iniciais.retorno('dc.rights.access'))
    dcrightsembargedtime = forms.CharField(max_length=100, label='Período de embargo',initial = dados_iniciais.retorno('dc.rights.embargedtime'))
    op_dcrightscreativecommons = [("Permite distribuição, remixagem, adaptação e criação a partir da obra, mesmo para fins comerciais, desde que seja atribuído o crédito ao autor da obra original (CC BY)","Permite distribuição, remixagem, adaptação e criação a partir da obra, mesmo para fins comerciais, desde que seja atribuído o crédito ao autor da obra original (CC BY)"),\
                                  ("Permite distribuição, remixagem, adaptação e criação a partir da obra, mesmo para fins comerciais, desde que seja atribuído o crédito ao autor da obra original e que as novas criações utilizem a mesma licença da obra original (CC BY-SA)","Permite distribuição, remixagem, adaptação e criação a partir da obra, mesmo para fins comerciais, desde que seja atribuído o crédito ao autor da obra original e que as novas criações utilizem a mesma licença da obra original (CC BY-SA)"),\
                                  ("Permite redistribuição, comercial ou não comercial, desde que a obra não seja modificada e que seja atribuído o crédito ao autor (CC BY-ND)","Permite redistribuição, comercial ou não comercial, desde que a obra não seja modificada e que seja atribuído o crédito ao autor (CC BY-ND)"),\
                                  ("Permite remixagem, adaptação e criação a partir da obra, desde que seja atribuído o crédito ao autor e que a nova criação não seja usada para fins comerciais (CC BY-NC)","Permite remixagem, adaptação e criação a partir da obra, desde que seja atribuído o crédito ao autor e que a nova criação não seja usada para fins comerciais (CC BY-NC)"),\
                                  ("Permite remixagem, adaptação e criação a partir da obra, para fins não comerciais, desde que seja atribuído o crédito ao autor da obra original e que as novas criações utilizem a mesma licença da obra original (CC BY-NC-SA)","Permite remixagem, adaptação e criação a partir da obra, para fins não comerciais, desde que seja atribuído o crédito ao autor da obra original e que as novas criações utilizem a mesma licença da obra original (CC BY-NC-SA)"),\
                                  ("Permite redistribuição não comercial, desde que seja atribuído o crédito ao autor e que a obra não seja alterada de nenhuma forma (CC BY-NC-ND)","Permite redistribuição não comercial, desde que seja atribuído o crédito ao autor e que a obra não seja alterada de nenhuma forma (CC BY-NC-ND)")]
    dcrightscreativecommons = forms.ChoiceField(choices=op_dcrightscreativecommons, label='Licença Creative Commons',initial = dados_iniciais.retorno('dc.rights.creativecommons'))
    op_dcdescriptionpublicationfees = [("A revista cobra taxa de submissão de artigos","A revista cobra taxa de submissão de artigos"),\
                                       ("A revista cobra taxa de processamento de artigos (APC)","A revista cobra taxa de processamento de artigos (APC)"),\
                                       ("A revista cobra taxa de submissão e de processamento de artigos","A revista cobra taxa de submissão e de processamento de artigos"),\
                                       ("A revista não cobra nenhuma taxa de publicação","A revista não cobra nenhuma taxa de publicação")]
    dcdescriptionpublicationfees = forms.ChoiceField(choices=op_dcdescriptionpublicationfees, label='Taxas de publicação',initial = dados_iniciais.retorno('dc.description.publicationfees'))
    dcdescriptionsubmissionfees = forms.CharField(max_length=100, label='Taxa de submissão de artigos',initial = dados_iniciais.retorno('dc.description.submissionfees'))
    dcdescriptionapc = forms.CharField(max_length=100, label='Taxa de processamento de artigos (APC)', initial = dados_iniciais.retorno('dc.description.apc'))
    dcdescriptioncodeofethics = forms.CharField(max_length=100, label='Código de ética',initial = dados_iniciais.retorno('dc.description.codeofethics'))
    dcdescriptionreferenceguidelines = forms.CharField(max_length=100, label='Padrão de normalização bibiográfico',initial = dados_iniciais.retorno('dc.description.referenceguidelines'))
    dcdescriptionplagiarismdetection = forms.CharField(max_length=100, label='Plataforma de detecção de plágio',initial = dados_iniciais.retorno('dc.description.plagiarismdetection') )
    dcdescriptiondigitalpreservation = forms.CharField(max_length=100, label='Estratégia de preservação digital', initial = dados_iniciais.retorno('dc.description.digitalpreservation'))
    op_dcrightsresearchdata = [("A revista exige que os autores publiquem os dados que deram origem à pesquisa em repositórios e/ou revistas de dados","A revista exige que os autores publiquem os dados que deram origem à pesquisa em repositórios e/ou revistas de dados"),\
                               ("A revista publica os dados que deram origem à pesquisa na própria revista","A revista publica os dados que deram origem à pesquisa na própria revista"),\
                               ("A revista não exige que os autores publiquem os dados que deram origem à pesquisa","A revista não exige que os autores publiquem os dados que deram origem à pesquisa")]
    dcrightsresearchdata = forms.ChoiceField(choices=op_dcrightsresearchdata, label='Exigência de disponibilização de dados de pesquisa',initial = dados_iniciais.retorno('dc.rights.researchdata'))
    op_dcdescriptionqualisarea = [("Revista não avaliada","Revista não avaliada"),\
                                  ("Administração pública e de empresas, Ciências contábeis e Turismo","Administração pública e de empresas, Ciências contábeis e Turismo"),\
                                  ("Antropologia / Arqueologia","Antropologia / Arqueologia"),\
                                  ("Arquitetura, urbanismo e design","Arquitetura, urbanismo e design"),\
                                  ("Artes","Artes"),\
                                  ("Astronomia / Física","Astronomia / Física"),\
                                  ("Biodiversidade","Biodiversidade"),\
                                  ("Biotecnologia","Biotecnologia"),\
                                  ("Ciência da computação","Ciência da computação"),\
                                  ("Ciência de alimentos","Ciência de alimentos"),\
                                  ("Ciência política e Relações internacionais","Ciência política e Relações internacionais"),\
                                  ("Ciências agrárias I","Ciências agrárias I"),\
                                  ("Ciências ambientais","Ciências ambientais"),\
                                  ("Ciências biológicas I","Ciências biológicas I"),\
                                  ("Ciências biológicas II","Ciências biológicas II"),\
                                  ("Ciências biológicas III","Ciências biológicas III"),\
                                  ("Ciências da religião e Teologia","Ciências da religião e Teologia"),\
                                  ("Comunicação e informação","Comunicação e informação"),\
                                  ("Direito","Direito"),\
                                  ("Economia","Economia"),\
                                  ("Educação","Educação"),\
                                  ("Educação física","Educação física"),\
                                  ("Enfermagem","Enfermagem"),\
                                  ("Engenharias I","Engenharias I"),\
                                  ("Engenharias II","Engenharias II"),\
                                  ("Engenharias III","Engenharias III"),\
                                  ("Engenharias IV","Engenharias IV"),\
                                  ("Ensino","Ensino"),\
                                  ("Farmácia","Farmácia"),\
                                  ("Filosofia","Filosofia"),\
                                  ("Geociências","Geociências"),\
                                  ("Geografia","Geografia"),\
                                  ("História","História"),\
                                  ("Interdisciplinar","Interdisciplinar"),\
                                  ("Linguística e literatura","Linguística e literatura"),\
                                  ("Matemática / Probabilidade e estatística","Matemática / Probabilidade e estatística"),\
                                  ("Materiais","Materiais"),\
                                  ("Medicina I","Medicina I"),\
                                  ("Medicina II","Medicina II"),\
                                  ("Medicina III","Medicina III"),\
                                  ("Medicina veterinária","Medicina veterinária"),\
                                  ("Nutrição","Nutrição"),\
                                  ("Odontologia","Odontologia"),\
                                  ("Planejamento urbano e regional / Demografia","Planejamento urbano e regional / Demografia"),\
                                  ("Psicologia","Psicologia"),\
                                  ("Química","Química"),\
                                  ("Saúde coletiva","Saúde coletiva"),\
                                  ("Serviço social","Serviço social"),\
                                  ("Sociologia","Sociologia"),\
                                  ("Zootecnia / Recursos pesqueiros","Zootecnia / Recursos pesqueiros")]
    dcdescriptionqualisarea = forms.ChoiceField(choices=op_dcdescriptionqualisarea, label='Área de avaliação Qualis-Periódicos',initial = dados_iniciais.retorno('dc.description.qualisarea'))
    op_dcdescriptionqualisclassification = [("Revista não avaliada","Revista não avaliada"),\
                                            ("A1","A1"),\
                                            ("A2","A2"),\
                                            ("A3","A3"),\
                                            ("A4","A4"),\
                                            ("B1","B1"),\
                                            ("B2","B2"),\
                                            ("B3","B3"),\
                                            ("B4","B4"),\
                                            ("C","C")]
    dcdescriptionqualisclassification = forms.ChoiceField(choices=op_dcdescriptionqualisclassification, label='Classificação Qualis-Periódicos',initial = dados_iniciais.retorno('dc.description.qualisclassification'))
    dcdescriptionsocialnetworks = forms.CharField(max_length=100, label='Redes Sociais',initial = dados_iniciais.retorno('dc.description.socialnetworks"'))
    dcrelationinformationservices = forms.CharField(max_length=100, label='Serviço de informação',initial = dados_iniciais.retorno('dc.relation.informationservices'))
    dcidentifierjournalsportaluri = forms.CharField(max_length=100, label='Portal de periódicos',initial = dados_iniciais.retorno('dc.identifier.journalsportaluri'))
    dcrelationoasisbr = forms.CharField(max_length=100, label='Artigos da revista no Portal oasisbr',initial = dados_iniciais.retorno('dc.relation.oasisbr'))
    
#    nome_portal = forms.CharField(max_length=100, label='Nome do portal de periódicos',)
#    url_portal =  forms.CharField(max_length=100, label='URL do portal de periódicos',)
#    inst_portal =  forms.CharField(max_length=100, label='Instituição responsável pelo portal de periódicos',)
#    org_subor_portal = forms.CharField(max_length=100, label='Organismo subordinado',)
#    adm_responsavel_portal = forms.CharField(max_length=100, label='Administrador responsável',)
#    email_portal = forms.CharField(max_length=100, label='E-mail do portal de periódicos',)
#    cep_portal = forms.CharField(max_length=100, label='Código Postal(CEP)',)
#    ed_estado_UF_portal = forms.ChoiceField(choices=op_estado_UF, label='Estado (UF)',)
#    ed_cidade_portal = forms.CharField(max_length=100, label='Cidade',)
#    ed_bairro_portal = forms.CharField(max_length=100, label='Bairro',)
#    ed_rua_portal = forms.CharField(max_length=100, label='Rua/quadra ou similar',)
#    ed_casa_portal = forms.CharField(max_length=100, label='Casa/Prédio/ Sala ou similar',)
#    ed_telefone_portal = forms.CharField(max_length=100, label='Telefone',)
#    revistas_portal = forms.CharField(max_length=100, label='Revistas do portal',)
#    
    
