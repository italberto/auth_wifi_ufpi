#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import logging
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


                    )
def auth(usuario,senha,driver_path):
    print(1)
    if usuario and senha:
        options = Options()
        #options.add_argument('--headless')
        print(2)
        driver = webdriver.Firefox(executable_path=driver_path,firefox_options=options)
        driver.get('https://login.ufpi.br:6082/php/uid.php?vsys=1&rule=0&url=http://conecta.ufpi.br%2f')
        print(3)
        user = driver.find_element_by_id('user')
        passwd = driver.find_element_by_id('passwd')
        submit = driver.find_element_by_id('submit')
        print(4)
        user.clear()
        passwd.clear()
        print(5)
        user.send_keys(usuario)
        passwd.send_keys(senha)
        submit.click()
        print(6)
        try:
            user = driver.find_element_by_id('user')
            print('x')
        except Exception:
            logging.info('Autenticação executada com sucesso!')
            print('y')
        print(7)
        driver.quit()
        print(8)