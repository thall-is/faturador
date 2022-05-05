from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import frame_to_be_available_and_switch_to_it
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import re

# setando as config do web driver chrome

driver = webdriver.Chrome(r"chromedriver.exe", options=options)
driver.implicitly_wait(20)

wait = WebDriverWait(driver, 60)

#loja vtex

site_login = 'https://{nome da loja}.myvtex.com/admin/checkout/#/orders?orderBy=creationDate,desc&per_page=100'

pedidos_faturados = 0

# funções

def loggin():

    try:
        email_path = ('#email')
        password_path = '#render-admin\.login-legacy\.home > div > div > div > div.ph7-ns.ph4.mb3 > div.mw6.mt7.center > div:nth-child(1) > div > div.mb5 > label > div > input'

        print('acessando o site...')

        driver.get(site_login)

        print('Iniciando login')
        test = 0
        email_box = driver.find_element(By.CSS_SELECTOR, email_path)
        email_box.click()
        print('Inserindo email...')

        #email para loggin

        print('{email de loggin}')
        email_box.send_keys('{email de loggin}' + Keys.ENTER)

        password_box = driver.find_element(By.CSS_SELECTOR, password_path)
        password_box.click()
        test = driver.find_element(By.CSS_SELECTOR, password_path).is_displayed()
        print('Inserindo a senha...')
        # senha referente a conta
        password_box.send_keys('{senha de loggin}' + Keys.ENTER)

        print('|Senha inserida!|')

    except NoSuchElementException:

        pass

    return test



    sleep(3)
    try:
        driver.implicitly_wait(0)
        sms = driver.find_element(By.XPATH,'//*[@id="render-admin.login-legacy.home"]/div/div/div/div[1]/div[2]/div[1]/div/div[1]').is_displayed()
        while sms == 1:
            print('Codigo sms requisitado !')
            codigo_de_acesso = input('|Insira o codigo |\n:')
            sms_patch = driver.find_element(By.XPATH, '//*[@id="requestsmscode_code"]')
            sms_patch.click()
            sms_patch.send_keys(codigo_de_acesso + Keys.ENTER)
            cod_invalid = driver.find_element(By.XPATH,'//*[@id="render-admin.login-legacy.home"]/div/div/div/div[1]/div[2]/div[1]/div/div[3]/label/div[2]').is_displayed()
            sms = driver.find_element(By.XPATH,'//*[@id="render-admin.login-legacy.home"]/div/div/div/div[1]/div[2]/div[1]/div/div[1]').is_displayed()

            if cod_invalid == 1:
                desc_cod_invalid = driver.find_element(By.XPATH, '//*[@id="render-admin.login-legacy.home"]/div/div/div/div[1]/div[2]/div[1]/div/div[3]/label/div[2]')
                print(desc_cod_invalid.text)
                sms_patch = driver.find_element(By.XPATH, '//*[@id="requestsmscode_code"]')
                webdriver.ActionChains(driver).double_click(sms_patch).perform()
                sms_patch.send_keys(Keys.DELETE)

    except NoSuchElementException:
        pass

    return test


def espera(v,s):
    for i in range(0,v):
        sleep(s)
        print('.')



while True:

            if loggin() == 1:

                print('carregando admin...')

                espera(5,1)

                print('|Admin carregado !|')
                driver.find_element(By.XPATH,'//*[@id="topbar-vtex"]/div[1]/div/div/button').click()

            print('entrando no iframe...')

            wait.until(
                frame_to_be_available_and_switch_to_it(
                    (By.XPATH, '//*[@id="app-content"]/main/iframe')
                )
            )

            print('|Dentro do iframe!|')

            espera(6,1)

            print('Atualizando pagina de pedidos')

            espera(3,1)

            driver.find_element(By.CSS_SELECTOR,'#app-container > div > div.st-container.st-effect-1 > div > div > div:nth-child(3) > div > div.container-fluid.totalizers-container > div:nth-child(1) > div > div > form > vt-filter-summary > div > small > span > span > a > i').click()

            espera(3,1)

            print('pedidos em "preparando entrega"')

            espera(6,1.2)

            driver.find_element(By.XPATH,'//*[@id="app-container"]/div/div[2]/div/div/div[3]/div/div[3]/div[1]/div/div/form/div[1]/button').click()

            espera(1,1)

            print('filtros')
            menu_lateral = driver.find_element(By.XPATH,'//*[@id="app-container"]/div/div[2]/div/div/div[3]/div/div[6]')
            menu_lateral.click()

            espera(1,1.5)

            driver.find_element(By.XPATH,'//*[@id="app-container"]/div/div[2]/div/div/div[3]/div/div[6]/vt-filter/div/div[4]/accordion/div/div[2]').click()

            espera(1,1.5)

            print('status')

            espera(1,1.5)

            print(".")
            driver.find_element(By.XPATH,'//*[@id="app-container"]/div/div[2]/div/div/div[3]/div/div[6]/vt-filter/div/div[4]/accordion/div/div[2]/div[2]/div/div/ul/li[2]/label/span/span').click()
            print('preparando entrega')

            espera(1,1.5)

            driver.execute_script("window.scrollTo(0, 450)")

            espera(1,1.5)

            print(".")

            #verificando se 'pedidos faturados' ou 'verificando fatura' esta marcado

            faturado_box = driver.find_element(By.XPATH,'//*[@id="app-container"]/div/div[2]/div/div/div[3]/div/div[6]/vt-filter/div/div[4]/accordion/div/div[2]/div[2]/div/div/ul/li[4]/label/input')
            faturado_box_selected = faturado_box.is_selected()

            verificando_faturado_box = driver.find_element(By.XPATH,'//*[@id="app-container"]/div/div[2]/div/div/div[3]/div/div[6]/vt-filter/div/div[4]/accordion/div/div[2]/div[2]/div/div/ul/li[3]/label/input')
            verificando_faturado_box_selected = verificando_faturado_box.is_selected()

            if faturado_box_selected == 1:

                faturado_box.click()

            elif verificando_faturado_box_selected == 1:

                verificando_faturado_box.click()

            driver.find_element(By.XPATH,'//*[@id="app-container"]/div/div[2]/div/div/div[3]/div/div[6]/vt-filter/div/div[4]/accordion/div/div[2]/div[2]/div/div/p/button[3]').click()
            print('confirmar')

            espera(1,1.5)

            print('.')
            driver.find_element(By.XPATH,'//*[@id="app-container"]/div/div[2]/div').click()
            print('X')

            espera(4,1)

            print('|Pedidos localizados !|')

            espera(3,1)

            print('Ordenando data crescente...')

            driver.find_element(By.XPATH,'//*[@id="app-container"]/div/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[1]/div/section/vt-table-header/div/div[2]/span/a/span').click()


            espera(5,1)

            Info_pedidos = driver.find_element(By.XPATH, '//*[@id="totalValueCountBRL"]')
            Receita_pedidos = driver.find_element(By.XPATH, '//*[@id="totalValueSumBRL"]')
            print('Pedidos para faturar' + ' ' + '=' + ' ' + (str(Info_pedidos.text)))
            print('Receita' + ' ' + '=' + ' ' + (str(Receita_pedidos.text)))

            print('\n\n\n')

            if Info_pedidos.text == 0:
                break

            # extraindo o numero de paginas nescessarias para percorrer todos os pedidos

            new_info_pedidos = Info_pedidos.text
            ponto = '.'
            new_info_pedidos = ''.join(x for x in new_info_pedidos if x not in ponto)
            Paginas_de_pedidos = int((int(new_info_pedidos)/100) + 1)

            list_pedidos = []

            # loop de extração de ID's de pedidos

            for i in range(0,(Paginas_de_pedidos)):

                pedidos_page = []

                pedidos = driver.find_elements(By.CSS_SELECTOR,"#app-container > div > div.st-container.st-effect-1 > div > div > div:nth-child(3) > div > div.container.body-container > div.row > div > div:nth-child(1) > div > section > div > a > span.td.mobile-fancy-title.relative")



                for j in range(0, len(pedidos)):
                    n = ''
                    n = pedidos[j].text
                    new_pedidos = ''
                    new_pedidos = (n)[:-7]
                    pedidos_page.append(new_pedidos)
                    list_pedidos.append(new_pedidos)

                print("*|--ID's-pagína-" + str(i) + "--|*\n")

                for k in range(0, len(pedidos_page)):
                    print('   ' + pedidos_page[k])

                print("\n*|-------END--------|*\n")

                print("total de ID's armazenados = " + str(len(list_pedidos)) + "\n.\n.\n.")

                driver.find_element(By.XPATH,'//*[@id="app-container"]/div/div[2]/div/div/div[3]/div/div[5]/div[1]/div/div/vt-pagination/div/div/div/ul/li[3]/a').click()
                espera(5,1)

            print("*|-------ID's-------|*\n")

            for i in range(0, len(list_pedidos)):
                print('   ' + list_pedidos[i])

            print("\n*|-------END--------|*\n")

            # na pagina do pedido inicia o loop de faturação

            for i in range(0,len(list_pedidos)):
                try:
                    driver.get('https://bijutotal.myvtex.com/admin/checkout/#/orders/'+list_pedidos[i])
                    espera(4,1)
                    wait.until(
                        frame_to_be_available_and_switch_to_it(
                            (By.XPATH, '//*[@id="app-content"]/main/iframe')
                        )
                    )
                    espera(4,1)

                    status_do_pedido = driver.find_element(By.XPATH,'//*[@id="app-container"]/div/div[2]/div/div/div[2]/div[3]/div[1]/div[4]/div/div/div[1]/div[1]/div/h4')

                    if status_do_pedido.text == 'Preparando entrega':

                        numero_da_nota = driver.find_element(By.XPATH,'//*[@id="app-container"]/div/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/h3/span[2]').text
                        numero_da_nota = numero_da_nota[1:7]

                        driver.execute_script("window.scrollTo(0, 400)")

                        espera(1,1.5)
                        driver.find_element(By.CSS_SELECTOR,'#app-container > div > div.st-container.st-effect-1 > div > div > div:nth-child(2) > div.container > div:nth-child(3) > div.span9 > div.packages-wrap > div > div.card-content > div > div.span8.pull-right > div > div > div > div.btn-actions.btn--no-padding > button').click()
                        print('faturar pacote')
                        espera(1,1.2)
                        driver.find_element(By.XPATH,'//*[@id="app-container"]/div/div[2]/div/div/div[2]/div[6]/div/div/div/div/div/vtex-sidebar-list-item[2]/div').click()
                        print('enviar nota manualmente')
                        espera(1,1.1)
                        print(numero_da_nota)
                        driver.find_element(By.XPATH, '//*[@id="invoice-number"]').click()
                        driver.find_element(By.XPATH,'//*[@id="invoice-number"]').send_keys(numero_da_nota)
                        espera(1,1.1)
                        driver.find_element(By.XPATH,'//*[@id="app-container"]/div/div[2]/div/div/div[2]/div[6]/div/div/div/div/div/form/fieldset[1]/div[6]/label/h4/span').click()
                        print('desabilitar informações de rastreio')
                        espera(1,1.1)
                        driver.find_element(By.XPATH,'//*[@id="app-container"]/div/div[2]/div/div/div[2]/div[6]/div/div/div/div/div/vtex-sidebar-footer/div/button/span').click()

                        print(list_pedidos[i] + ' faturado')

                        pedidos_faturados = pedidos_faturados + 1

                        espera(4,1)
                except NoSuchElementException:
                    pass
            print('pedidos faturados = ' + str(pedidos_faturados) + "\n\n\n***")

            pedidos.clear()
