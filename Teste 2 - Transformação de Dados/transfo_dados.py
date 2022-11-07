import tabula
import pandas
from zipfile import ZipFile, ZIP_DEFLATED

#Diretórios dos Arquivos
file_pdf = 'Teste 2 - Transformação de Dados\Arquivo PDF\Anexo I - Lista completa de procedimentos.pdf'
file_csv = 'Teste 2 - Transformação de Dados\Arquivo CSV\Anexo I - Lista completa de procedimentos.csv'
file_zip = 'Teste 2 - Transformação de Dados\Arquivo ZIP'

#Lendo o PDF
pdf = tabula.read_pdf(file_pdf, pages='3-180', multiple_tables=False)

#Criando um Novo DataFraame
data_frame = pandas.concat(pdf)

#Copiando DataFrame para fazer as modificações sem perder o original - Substituindo os Nomes nas Colunas
data_frame_copia = data_frame.rename(
    columns={
        'OD': 'Seg. Odontológica',
        'AMB': 'Seg. Ambulatorial'
    }
)

#Novos Valores para as Colunas
new_OD = {'OD': 'Seg. Odontológica'}
new_AMB = {'AMB': 'Seg. Ambulatorial'}

#Substituindo os valores nas colunas
data_frame_copia['Seg. Odontológica'] = data_frame_copia['Seg. Odontológica'].map(new_OD)
data_frame_copia['Seg. Ambulatorial'] = data_frame_copia['Seg. Ambulatorial'].map(new_AMB)

#Retirandos as Linahs Duplicadas - As linhas de Cabeçalho das Tabelas
data_frame_final = data_frame_copia.drop_duplicates()

#Criando o arquivo CSV
data_frame_final.to_csv(file_csv, index=False)

#Criando o Zip e adicionando dentro dele
with ZipFile(file_zip + "/" + "Teste_Daniel.zip", "w", compression=ZIP_DEFLATED) as compactado:
    compactado.write(file_csv, "Anexo I - Lista completa de procedimentos.csv")