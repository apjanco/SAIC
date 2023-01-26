from pathlib import Path

import srsly
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

def load_page():
    driver = webdriver.Firefox()

    driver.get('https://www.senado.leg.br/atividade/baseshist/bh.asp#/')
    select_archive = driver.find_element(By.XPATH, '//*[@id="sel_base"]/option[16]')
    select_archive.click()

    enter_search = driver.find_element(By.XPATH, '//*[@id="txtPesquisa"]')
    enter_search.send_keys("origem");

    full_search = driver.find_element(By.XPATH,'//*[@id="cad"]/div[2]/input[2]')
    full_search.click()


/html/body/div[6]/div[1]/div/div/p[13]/a[4]
/html/body/div[6]/div[1]/div/div/p[13]/a[5]

if __name__ == "__main__":
    load_page()



