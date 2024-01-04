from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


# marca checkbox para acessar todos
def checkbox_for_all(driver):
    
    checkbox = driver.find_element(By.ID, "colunas-ranking__todos")
    driver.execute_script("arguments[0].click();", checkbox)


#salva numa lista
def head_catch(driver):

    head = driver.find_element(By.CLASS_NAME, 'default-fiis-table__container__table__head')
    HEAD = []
    head_elementos = head.find_elements(By.TAG_NAME, "th")
    for th in head_elementos:
        HEAD.append(th.text)

    return HEAD


# todo o conteudo da tabela
def body_catch(driver):

    body = driver.find_element(By.CLASS_NAME, 'default-fiis-table__container__table__body.skeleton-content')
    body_lines = body.find_elements(By.TAG_NAME, "tr")

    body_elements = []

    for line in body_lines:
        columns = line.find_elements(By.TAG_NAME, "td")
        row_data = [column.text for column in columns]
        body_elements.append(row_data)
    
    return body_elements
