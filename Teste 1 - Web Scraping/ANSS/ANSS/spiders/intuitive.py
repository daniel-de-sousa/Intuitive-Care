import scrapy


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