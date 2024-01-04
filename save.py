import csv
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

#busca
driver.get("https://www.fundsexplorer.com.br/ranking")
driver.implicitly_wait(0.5)

# marca checkbox para acessar todos
checkbox = driver.find_element(By.ID, "colunas-ranking__todos")
driver.execute_script("arguments[0].click();", checkbox)

#salva numa lista
head = driver.find_element(By.CLASS_NAME, 'default-fiis-table__container__table__head')
HEAD = []
head_elementos = head.find_elements(By.TAG_NAME, "th")
for th in head_elementos:
    HEAD.append(th.text)

# todo o conteudo da tabela
body = driver.find_element(By.CLASS_NAME, 'default-fiis-table__container__table__body.skeleton-content')
body_lines = body.find_elements(By.TAG_NAME, "tr")

body_elements = []

for line in body_lines:
    columns = line.find_elements(By.TAG_NAME, "td")
    row_data = [column.text for column in columns]
    body_elements.append(row_data)


# escreve csv
nome_arquivo_csv = 'teste.csv'
caminho = '/home/matheus/Documentos/0003/cods/CsvRequest/output/'

if not os.path.exists(caminho):
    os.makedirs(caminho)

caminho_completo = os.path.join(caminho, nome_arquivo_csv)

with open(caminho_completo, 'w', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    escritor_csv.writerows([HEAD])
    escritor_csv.writerows(body_elements)

print(f'Arquivo "{nome_arquivo_csv}" criado.')


driver.quit()