# Teste 1 - Web Scraping

**Web Scraping** consiste na raspagem de dados da web.

No caso, o que se deseja é realizar o download de arquivos no domínio **[www.gov.br](https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude "Agência Nacional de Saúde Suplementar (ANSS)")**, e depois compactados para um arquivo **.zip**

Para isso, será utilizado da linguagem Python, utilizando de alguns módulos para algumas tarefas:

**Scrapy**: Para realizar a conexão com o site e identificar os elementos que se deseja fazer o download

**Request**: Para poder se obter as informações do arquivo para ser possível salvar em um novo arquivo

**ZipFile**: Para realizar a compactação de arquivos.

**Os**: Para a manipulação de diretórios dentro do sistema operacional

O Processo se dara da seguinte forma:

1. Se conectar com o Site
1. Identificar os Elementos
1. Captar o Nome e o Link do arquivo com o **Scrapy**
1. Através das Informações Captadas criar um novo arquivo local
1. Identificar a quntidade de Arquivos locais para inteirar sobre eles para adicionar a um Arquivo .zip

**Ps**: Para garantir a Existência da Pasta **Arquivos** o Programa já foi executado antes de Subir para o GitHub