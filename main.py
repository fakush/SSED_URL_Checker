from datetime import datetime

import httplib2
import socket
import time
from selenium import webdriver
import whois

h = httplib2.Http(".cache", disable_ssl_certificate_validation=True)

#Para armar modulo Nic
#https://nic.ar/whois
#https://pypi.org/project/python-whois/


# Poner Urls a Chechear
listUrls = ['infoemergencias.buenosaires.gob.ar', 'testra2.buenosaires.gob.ar', 'colonias.buenosaires.gob.ar', 'cmctgps1.buenosaires.gob.ar', 'bienes.buenosaires.gob.ar', 'clipping.buenosaires.gob.ar', 'formularios.buenosaires.gob.ar', 'mandatarios.buenosaires.gob.ar', 'moda.buenosaires.gob.ar', 'rondaeditorial.buenosaires.gob.ar', 'cmct.buenosaires.gob.ar', 'cmctgps2.buenosaires.gob.ar', 'datosestudiantes.buenosaires.gob.ar', 'expresometro.buenosaires.gob.ar', 'serviciobicicletas.buenosaires.gob.ar', 'bibliotecateatrocolon.buenosaires.gob.ar', 'baset.buenosaires.gob.ar', 'estatico-boletines.buenosaires.gob.ar', 'blogs.buenosaires.gob.ar', 'mapa1.buenosaires.gob.ar', 'rs1.buenosaires.gob.ar', 'estatico.buenosaires.gob.ar', 'pdsl.buenosaires.gob.ar', 'prrac2.buenosaires.gob.ar', 'acceder.buenosaires.gob.ar', 'escueladomi1media.buenosaires.gob.ar', 'feriadelibrovirtual.buenosaires.gob.ar', 'indexer.webbeta.buenosaires.gob.ar', 'notificaciones.buenosaires.gob.ar', 'palermolimpio.buenosaires.gob.ar', 'searcher.webbeta.buenosaires.gob.ar', 'telesalud.buenosaires.gob.ar', 'tgplaneamiento.buenosaires.gob.ar', 'veranociudad.buenosaires.gob.ar', 'webbeta.buenosaires.gob.ar', 'sig.buenosaires.gob.ar', 'yoreciclo.buenosaires.gob.ar', 'transparencia.buenosaires.gob.ar', 'pmcaba.buenosaires.gob.ar', 'bicentenariociudad.buenosaires.gob.ar', 'planhidraulico.buenosaires.gob.ar', 'sp.buenosaires.gob.ar', 'haciendoelcolond.buenosaires.gob.ar', 'definitivo.buenosaires.gob.ar', 'festivalem.buenosaires.gob.ar', 'redcomenius.buenosaires.gob.ar', 'tablero.buenosaires.gob.ar', 'bo.buenosaires.gob.ar']

#Nombre del Archivo a guardar
fileName = 'primer_lote_sinVPN.txt'

#Encabezado del Archivo de texto
header = 'Lista URLS: Primer Lote - Sin VPN'

#VPN = Valores conVpn o sinVpn
vpn = 'sinVpn'

count = 0

def getWebImg(url, counter, prefix):
    options = webdriver.ChromeOptions()
    options.headless = False
    driver = webdriver.Chrome('/Utils/chromedriver.exe')
    driver.get('http://' + url)
    time.sleep(1)
    print("tomando captura de " + str(counter +1 ) + " " + url)
    nameString1 = url.replace('.', '-')
    nameString = nameString1.replace('/', '-')
    driver.get_screenshot_as_file('/ProcesosTemp/' + str(counter + 1) + "-" + vpn + "-" + prefix + nameString + '_screenshot.png')
    driver.quit()
    print("end...")

def procesoURL(prefix, url, counter, respuesta):
    print("\n" + str(counter + 1) + " " + prefix + url + " " + respuesta)
    print("\n"+ str(counter + 1) + "," + prefix + url + "," + respuesta, file=f)

with open(fileName, 'w') as f:
    print(header, file=f)
    for each in listUrls:
        try:
            response, content = h.request('http://' + listUrls[count])
            procesoURL("http://", listUrls[count], count, str(response.status))
            getWebImg(listUrls[count], count, "")

        except httplib2.ServerNotFoundError:
            procesoURL("http://", listUrls[count], count, "SERVER NOT FOUND ERROR")

        except (httplib2.HttpLib2Error, socket.error) as ex:
            procesoURL("http://", listUrls[count], count, "TIMEOUT ERROR")

        try:
            response, content = h.request('http://www.' + listUrls[count])
            procesoURL("http://www.", listUrls[count], count, str(response.status))
            getWebImg(listUrls[count], count, "www-")

        except httplib2.ServerNotFoundError:
            procesoURL("http://www.", listUrls[count], count, "SERVER NOT FOUND ERROR")

        except (httplib2.HttpLib2Error, socket.error) as ex:
            procesoURL("http://", listUrls[count], count, "TIMEOUT ERROR")

        count = count + 1

