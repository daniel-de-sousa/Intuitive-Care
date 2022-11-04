import os
import scrapy
import requests
from zipfile import ZipFile, ZIP_DEFLATED

#Definindo o Endereço de onde os arquivos serão armazenados
local = 'ANSS\Arquivos'

#Função para Baixar os Arquivos
def download(title, url):
    #Realizando a Requisição do Servidor - Obtendo os Dados do arquivo
    requisicao = requests.get(url)
    
    #Verificando se Pode Continuar com o Processor de Baixar os Dados do Arquivo
    if requisicao.status_code == requests.codes.OK:
        #Combinando as Informações do Nome do Arquivo - Combinado Nome e Extensão
        nome = (title + '.' + (url.split('.'))[-1])

        #Combinando as Informações de Local com Nome para Passar na Hora de Salvar o Arquivo
        nome_local = os.path.join(local, nome)

        #Abrindo um Novo Arquivo para Salvar as Informações
        with open(nome_local, 'wb') as novo_arquivo:
            novo_arquivo.write(requisicao.content)

    else:
        requisicao.raise_for_status()

#Função para Compactar os Arquivos
def compactar():
    #Pegando a Quantida de Arquivos na Pasta para inteirar sobre eles
    quantidade = os.listdir(local)

    #Criando o arquivo zip e Adicionando os Arquivos Dentro
    with ZipFile(local + "/" + 'Arquivos_Compactados.zip', 'w', compression=ZIP_DEFLATED) as compactado:
        for item in quantidade:
            compactado.write(local + "/" + item, item)

class IntuitiveSpider(scrapy.Spider):
    #Nome da Spider
    name = 'intuitive'

    #Site onde a spider vai procurar as informações
    start_urls = ['https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude']

    #Função executada assim que a spider for chamada
    def parse(self, response):

        #Funçõa par Inteirar sobre os arquivos que serão Baixados - Pegando Nome e Link
        for box in  response.css('.callout')[2:7]:
            #Pegando o Nome - Retira a Parte Final e Todos os Espaços Desnecessários
            title = (box.css('.callout+ .callout .internal-link::text').get().split('('))[0].strip()

            #Pegando o Link do Arquivo - Busca o Elemento Âncora do HTML e pega o que estiver no atribúto href
            link = box.css('.callout+ .callout .internal-link').attrib['href']

            #Chamando a Função para Baixar o Arquivo que Foi Identificado
            download(title, link)
        
        #Chamando a Função para Compactar
        compactar()
