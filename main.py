from selenium import webdriver
from selenium_control import *
from dot_env_control import *
from csv_writter import *

# =-=-=-=-=-==-=-=-=-=-==-=-=-=-=-==-=-=-=-=-=
# WEBDRIVERS

'''=-=-=-=-=-= Edge =-=-=-=-=-= '''
# options = webdriver.EdgeOptions()
# driver = webdriver.Edge(options=options)

'''=-=-=-=-=-= Chrome =-=-=-=-=-= '''
# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(options=options)

'''=-=-=-=-=-= firefox =-=-=-=-=-= '''
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

# =-=-=-=-=-==-=-=-=-=-==-=-=-=-=-==-=-=-=-=-=

driver.get('https://www.fundsexplorer.com.br/ranking')
driver.implicitly_wait(0.5)

checkbox_for_all(driver)
HEAD = head_catch(driver)
body_elements = body_catch(driver)
write_csv(HEAD, body_elements)

driver.quit()