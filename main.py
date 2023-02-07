from pathlib import Path
import time
import srsly
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tqdm import trange

driver = webdriver.Firefox()
def load_page():
    
    driver.get('https://www.senado.leg.br/atividade/baseshist/bh.asp#/')
    select_archive = driver.find_element(By.XPATH, '//*[@id="sel_base"]/option[16]')
    select_archive.click()

    enter_search = driver.find_element(By.XPATH, '//*[@id="txtPesquisa"]')
    enter_search.send_keys("origem");

    full_search = driver.find_element(By.XPATH,'//*[@id="cad"]/div[2]/input[2]')
    full_search.click()

def get_data():
    data = {}
    start_page = 5001
    final_page = 6000 #7272
    page = 1
    for page in trange(start_page,final_page):
        # scrape data
        try:
            records = driver.find_elements(By.TAG_NAME, 'p')
            for record in records:
                if 'NOME' in record.text:
                    NOME = record.text[record.text.find('NOME')+ len('NOME'):record.text.find('ENDEREÇO')].strip()
                    data[NOME] = record.text
                    
            # open next page
            time.sleep(2)
            driver.execute_script(f"javascript:Paginacao({page + 1})")
            #document.frmStatus.intPag.value = pagina;
            #document.frmStatus.submit();
            time.sleep(4)
            if (page % 200) == 0:
                srsly.write_json(f'{page}_data.json', data)
        except Exception as e:
            print(e)
    srsly.write_json(f'{start_page}_{final_page}_data.json', data)
    driver.close()

if __name__ == "__main__":
    load_page()
    time.sleep(2)
    data = get_data()
    



# IDENTIFICAÇÃO

#      ORIGEM: L001 DATA: 20/02/86 FORMUL: 001 DV: 4 TIPO: 10  31/10/86
# NOME

#      Eliza Nunes da Costa
# ENDEREÇO

#      Carnauba-Torta-Trairi-Ce
# LOCALIZAÇÃO

#      MUNICIPIO: TRAIRI                           UF: CE   CEP: 62690
# DADOS PESSOAIS

#      SEXO        : 02 - FEMININO
#      MORADOR     : 01 - ZONA RURAL
#      INSTRUÇÃO   : 05 - SEGUNDO GRAU COMPLETO
#      ESTADO CIVIL: 01 - SOLTEIRA
#      FAIXA ETÁRIA: 02 - 15 A 19 ANOS
#      FAIXA RENDA : 08 - SEM RENDIMENTO
#      ATIVIDADE   : 11 - OUTRAS ATIVIDADES
# CATÁLOGO

#      POLITICA EDUCACIONAL.
#      LIVRO DIDATICO, MATERIAL ESCOLAR.
# SUGESTÃO

#      A minha opinião é que mudasse com o livro descartável para que
#      pudéssemos estudar mais a vontade.

