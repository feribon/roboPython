# importando bibliotecas
import pandas as pd
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
# importando arquivo do excel
abrirTabela = pd.read_excel('listaFoneJunto.xlsx')
# abrindo o whatsapp no google chrome, quando abrir vc tem q instalar a extensao wa web whatsapp plus e ativar msg para nao contatos
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(120)
# for in navegando pela coluna nome da planilha do excel
for x in abrirTabela['nome']:
    # acha o local e clica pra inserir o numero
    campo_pesquisa = driver.find_element_by_xpath(
        '//div[contains(@class,"_2n-zq")]')
    time.sleep(1)
    campo_pesquisa.click()
    time.sleep(1)
    campo_numero = driver.find_element_by_tag_name('input')
    time.sleep(1)
    campo_numero.send_keys(f'{x[0:11]}')
    campo_numero.send_keys(Keys.ENTER)
    time.sleep(1)
    try:
        # se o contato nao tem whatsapp, fecha a tela do erro
        campo_erro = driver.find_element_by_xpath(
            '//div[contains(@class,"VtaVl -TvKO")]')
        time.sleep(1)
        campo_erro.click()
        time.sleep(1)
    except:
        # se nao cair na tela do erro envia a mensagem
        campo_mensagem = driver.find_elements_by_xpath(
            '//div[contains(@class,"copyable-text selectable-text")]')
        time.sleep(1)
        campo_mensagem[1].send_keys(
            f'aeee {x[11:]} estou testando um esquema de msg automatica')
        campo_mensagem[1].send_keys(Keys.ENTER)
