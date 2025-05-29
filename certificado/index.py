import openpyxl
from docxtpl  import DocxTemplate 
import datetime

# acessar a planilha e consumir dados

caminho = 'student_data.xlsx'
pasta_trabalho = openpyxl.load_workbook(caminho)
planilha = pasta_trabalho.active

valores = list(planilha.values)

print(valores)

# gerando o certificado preenchido

doc = DocxTemplate('certificate.docx')

for x in valores[1:]:
    doc.render({
        'nome':x[0],
        'curso':x[1],
        'data':x[2].strftime('%d/%m%Y'),
        'instrutor':x[3]
    })
    
    nome = f'certificado de {x[0]}.docx'
    doc.save(nome)