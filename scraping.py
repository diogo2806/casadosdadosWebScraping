import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from urllib3.util import wait
import pyautogui

def buscar_empresas():
    driver = webdriver.Chrome()
    janela_principal = driver.current_window_handle

    driver.maximize_window()  # maximiza a janela do navegador
    driver.get("https://casadosdados.com.br/solucao/cnpj/pesquisa-avancada")
    time.sleep(5)
    driver.switch_to.window(janela_principal)

    # Role a página até o final
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Role a página para cima
    driver.execute_script("window.scrollTo(0, -document.body.scrollHeight);")


    # preencher campos
    #text_razao_social(driver)
    #text_cnae(driver)
    #text_natureza_juridica(driver)
    #text_estado_uf(driver)
    #text_municipio(driver)
    #text_bairro(driver)
    #text_cep(driver)
    #text_ddd(driver)
    text_data_de_abertura_a_partir_de(driver)
    text_data_de_abertura_ate(driver)
    text_capital_social_a_partir_de(driver)
    text_capital_social_ate(driver)
    #incluir_atividade_secundaria(driver)
    #somente_mei(driver)
    #somente_matriz(driver)
    #excluir_mei(driver)
    #somente_filial(driver)
    #com_contato_telefonico(driver)
    #somente_celular(driver)
    #somente_fixo(driver)
    #com_email(driver)


    # pesquisar

    clicar_no_botao_pesquisar(driver)
    time.sleep(5)

    # Verifica a quantidade de dados existentes na data atual
    total_de_dados = verificar_existencia(driver)
    print('total_de_dados:')
    print(total_de_dados)
    print('sucesso total_de_dados')

    # Se não houver dados na pesquisa atual, retorna um valor Falso.
    if total_de_dados == 0:
        return False

    # Define o número de páginas
    paginas = numero_de_paginas(total_de_dados)
    print('numero_de_paginas:')
    print(paginas)
    print('sucesso numero_de_paginas')

    obter_links(driver, paginas)
    time.sleep(60)





#funções para preencher os campos
def clicar_no_botao_pesquisar(driver):
    try:
        driver.find_element(by=By.XPATH,
                               value='/html/body/div[2]/div/div/div[2]/section/div[6]/div/div[1]/button[1]').click()
        print('sucesso clicar_no_botao_pesquisar')

    except Exception:
        print("Erro ao tentar clicar em pesquisar, tentando novamente...")
        clicar_no_botao_pesquisar(driver)

def text_razao_social(driver):
    try:
        cnpj_div = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[2]/section/div[2]/div[1]/section/div/div/div/div/div/div[1]/input')))
        cnpj_div.click()
        cnpj_div.send_keys('')
        print('sucesso text_razao_social')

    except Exception:
        print("Erro ao tentar clicar em Razão Social ou Nome Fantasia, tentando novamente...")
        text_razao_social(driver)

def text_cnae(driver):
    try:
        cnae_div = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[2]/section/div[2]/div[2]/section/div/div/div/div/div[1]/input')))
        cnae_div.click()
        cnae_div.send_keys('0113000')

        cnae_div_select = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="__layout"]/div/div[2]/section/div[2]/div[2]/section/div/div/div/div/div[2]/div/a[1]/span')))
        cnae_div_select.click()
        print('sucesso text_cnae')

    except Exception:
        print("Erro ao tentar clicar em Atividade Principal (CNAE), tentando novamente...")
        text_razao_social(driver)


def text_natureza_juridica(driver):
    try:
        natureza_juridica_div = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[2]/section/div[2]/div[3]/section/div/div/div/div/div[1]/input')))
        natureza_juridica_div.click()
        natureza_juridica_div.send_keys('1333')

        natureza_juridica_div_select = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="__layout"]/div/div[2]/section/div[2]/div[3]/section/div/div/div/div/div[2]/div/a/span')))
        natureza_juridica_div_select.click()

        natureza_juridica_div.click()
        natureza_juridica_div.send_keys('2038')

        natureza_juridica_div_select = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH,
             '//*[@id="__layout"]/div/div[2]/section/div[2]/div[3]/section/div/div/div/div/div[2]/div/a/span')))
        natureza_juridica_div_select.click()
        print('sucesso text_natureza_juridica')


    except Exception:
        print("Erro ao tentar clicar em Natureza Jurídica, tentando novamente...")
        text_natureza_juridica(driver)


def text_estado_uf(driver):
    try:
        uf_div = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[2]/section/div[3]/div[2]/div/div/div/div/div[1]/input')))
        uf_div.click()
        uf_div.send_keys('rio de janeiro')

        uf_div_select = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="__layout"]/div/div[2]/section/div[3]/div[2]/div/div/div/div/div[2]/div/a')))
        uf_div_select.click()
        print('sucesso text_estado_uf')



    except Exception:
        print("Erro ao tentar clicar em Estado (UF), tentando novamente...")
        text_estado_uf(driver)


def text_municipio(driver):
    try:
        municipio_div = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[2]/section/div[3]/div[3]/div/div/div/div/div[1]/input')))
        municipio_div.click()
        municipio_div.send_keys('itaguai')

        municipio_div_select = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="__layout"]/div/div[2]/section/div[3]/div[3]/div/div/div/div/div[2]/div/a')))
        municipio_div_select.click()
        print('sucesso text_municipio')



    except Exception:
        print("Erro ao tentar clicar em Municipio, tentando novamente...")
        text_municipio(driver)


def text_bairro(driver):
    try:
        bairro_div = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[2]/section/div[3]/div[4]/div/div/div/div/div[1]/input')))
        bairro_div.click()
        bairro_div.send_keys('centro', Keys.RETURN)


        print('sucesso text_bairro')



    except Exception:
        print("Erro ao tentar clicar em Bairro, tentando novamente...")
        text_bairro(driver)

def text_cep(driver):
    try:
        cep_div = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[2]/section/div[3]/div[5]/div/div/div/div/div[1]/input'
                                                                                            '')))
        cep_div.click()
        cep_div.send_keys('23815650', Keys.RETURN)
        print('sucesso text_cep')

    except Exception:
        print("Erro ao tentar clicar em CEP, tentando novamente...")
        text_cep(driver)

def text_ddd(driver):
    try:
        ddd_div = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[2]/section/div[4]/div[1]/div/div/div/div/div[1]/input')))
        ddd_div.click()
        ddd_div.send_keys('21', Keys.RETURN)
        print('sucesso text_ddd')



    except Exception:
        print("Erro ao tentar clicar em DDD, tentando novamente...")
        text_ddd(driver)

def text_data_de_abertura_a_partir_de(driver):
    try:
        data_div = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[2]/section/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/input')))
        data_div.click()
        data_div.send_keys('21/01/2021')
        print('sucesso text_data_de_abertura_a_partir_de')


    except Exception:
        print("Erro ao tentar clicar em Data de Abertura - A partir de, tentando novamente...")
        text_data_de_abertura_a_partir_de(driver)

def text_data_de_abertura_ate(driver):
    try:
        data_div = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[2]/section/div[4]/div[2]/div/div[2]/div/div/div/div[1]/div/input')))
        data_div.click()
        data_div.send_keys('21/02/2021')
        print('sucesso text_data_de_abertura_ate')


    except Exception:
        print("Erro ao tentar clicar em Data de Abertura - Até, tentando novamente...")
        text_data_de_abertura_ate(driver)

def text_capital_social_a_partir_de(driver):
    try:
        capital_social_div = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[2]/section/div[4]/div[3]/section/div/div/input')))
        capital_social_div.click()
        capital_social_div.send_keys('1000')
        print('sucesso text_capital_social_a_partir_de')


    except Exception:
        print("Erro ao tentar clicar em Capital Social - A partir de, tentando novamente...")
        text_capital_social_a_partir_de(driver)


def text_capital_social_ate(driver):
    try:
        capital_social_div = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[2]/section/div[4]/div[4]/div/div/input')))
        capital_social_div.click()
        capital_social_div.send_keys('10000')
        print('sucesso text_capital_social_ate')


    except Exception:
        print("Erro ao tentar clicar em Capital Social - Até, tentando novamente...")
        text_capital_social_ate(driver)

def incluir_atividade_secundaria(driver):
    try:
        check_div = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[2]/section/div[2]/div[2]/section/label/span[1]')))
        check_div.click()

        print('sucesso incluir_atividade_secundaria')


    except Exception:
        print("Erro ao tentar clicar em Incluir Atividade Secundária, tentando novamente...")
        incluir_atividade_secundaria(driver)

def somente_mei(driver):
    try:
        check_div = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[2]/section/div[5]/div[1]/div[1]/div/div/label[1]/span[1]')))
        check_div.click()

        print('sucesso somente_mei')


    except Exception:
        print("Erro ao tentar clicar em Somente MEI, tentando novamente...")
        somente_mei(driver)

def somente_matriz(driver):
    try:
        check_div = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[2]/section/div[5]/div[1]/div[2]/div/div/label[1]/span[1]')))
        check_div.click()

        print('sucesso somente_matriz')


    except Exception:
        print("Erro ao tentar clicar em Somente Matriz, tentando novamente...")
        somente_matriz(driver)


def excluir_mei(driver):
    try:
        check_div = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[2]/section/div[5]/div[1]/div[1]/div/div/label[2]/span[1]')))
        check_div.click()

        print('sucesso excluir_mei')


    except Exception:
        print("Erro ao tentar clicar em Excluir MEI, tentando novamente...")
        excluir_mei(driver)


def somente_filial(driver):
    try:
        check_div = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[2]/section/div[5]/div[1]/div[2]/div/div/label[2]/span[1]')))
        check_div.click()

        print('sucesso somente_filial')


    except Exception:
        print("Erro ao tentar clicar em Somente filial, tentando novamente...")
        somente_filial(driver)


def com_contato_telefonico(driver):
    try:
        check_div = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[2]/section/div[5]/div[2]/div[1]/div/div/label[1]/span[1]')))
        check_div.click()

        print('sucesso com_contato_telefonico')


    except Exception:
        print("Erro ao tentar clicar em Com contato de telefone, tentando novamente...")
        com_contato_telefonico(driver)


def somente_celular(driver):
    try:
        check_div = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[2]/section/div[5]/div[2]/div[2]/div/div/label[1]/span[1]')))
        check_div.click()

        print('sucesso somente_celular')


    except Exception:
        print("Erro ao tentar clicar em Com celular, tentando novamente...")
        somente_celular(driver)


def somente_fixo(driver):
    try:
        check_div = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[2]/section/div[5]/div[2]/div[1]/div/div/label[2]/span[1]')))
        check_div.click()

        print('sucesso somente_fixo')


    except Exception:
        print("Erro ao tentar clicar em Somente fixo, tentando novamente...")
        somente_fixo(driver)


def com_email(driver):
    try:
        check_div = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[2]/section/div[5]/div[2]/div[2]/div/div/label[2]/span[1]')))
        check_div.click()

        print('sucesso com_email')


    except Exception:
        print("Erro ao tentar clicar em Com e-mail, tentando novamente...")
        com_email(driver)

# Esta função define o número de páginas de acordo com a quantidade total de elementos no dia.      (OK)
def verificar_existencia(driver):
    time.sleep(1.5)
    try:

        if (driver.find_element(by=By.XPATH,
                                   value='/html/body/div[2]/div/div/div[2]/section/div[9]/div[1]/div/div/div/div/p').text) != 'Nenhum resultado para sua pesquisa':
            total_resultados = driver.find_element(by=By.XPATH,
                                                      value='/html/body/div[2]/div/div/div[2]/section/div[9]/div[1]/div/div/div/div/p/b').text  # captura o valor dos resultados
            total_resultados = int(total_resultados.replace('.', ''))


            return total_resultados

        else:
            return 0
    except Exception:
        print("Erro ao tentar verificar o resultado existe, tentando novamente...")
        verificar_existencia(driver)


# Esta função define o número de páginas de acordo com a quantidade total de elementos no dia.      (OK)
def numero_de_paginas(elementos):
    if elementos > 1000:
        return 50
    elif (elementos <= 20) and (elementos > 0):
        return 1
    elif elementos == 0:
        return 0
    return int(math.ceil(elementos / 20))


def obter_links(driver, paginas):
    try:
        lista_de_links = []

        for n in range(1, paginas):
            for i in range(1, 21):
                # encontra o elemento com o xpath especificado
                elemento = driver.find_element(by=By.XPATH,
                                                      value='/html/body/div[2]/div/div/div[2]/section/div[9]/div[1]/div/div/div/div/div[%d]/article/div/div/p/a' % (
                                                          i))
                # extraia o atributo href
                link = elemento.get_attribute("href")
                # adicione o link a uma lista
                lista_de_links.append(link)
                # imprima a lista de links

            avancar_pagina(driver)

        print(lista_de_links)




        print('sucesso obter_links')


    except Exception:
        print("Erro ao tentar obter links, tentando novamente...")
        obter_links(driver)


# Esta função faz o papel de avançar para a próxima página.                 (OK)
def avancar_pagina(driver):
    time.sleep(1)
    try:
        driver.find_element(by=By.XPATH,
                            value='//*[@id="__layout"]/div/div[2]/section/div[8]/div/nav/a[2]').click()


    except Exception:
        print("Erro ao tentar avançar a página, tentando novamente...")
        avancar_pagina(driver)