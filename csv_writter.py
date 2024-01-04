from dot_env_control import *
import csv
import os

FOLDER_PATH = ENV['FOLDER_PATH']
FILE_NAME = ENV['FILE_NAME']

def write_csv(HEAD, body_elements):
    if not os.path.exists(FOLDER_PATH):
        os.makedirs(FOLDER_PATH)

    caminho_completo = os.path.join(FOLDER_PATH, FILE_NAME)

    with open(caminho_completo, 'w', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        escritor_csv.writerows([HEAD])
        escritor_csv.writerows(body_elements)

    print(f'Arquivo "{FILE_NAME}" criado.')
