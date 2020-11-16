from datetime import datetime

import httplib2
import socket
import time
import selenium
from selenium import webdriver
import whois
from selenium.common.exceptions import WebDriverException

h = httplib2.Http(".cache", disable_ssl_certificate_validation=True)

#Para armar modulo Nic
#https://nic.ar/whois


# Poner Urls a Chechear
listUrls = ['infoemergencias.buenosaires.gob.ar', 'testra2.buenosaires.gob.ar', 'colonias.buenosaires.gob.ar', 'cmctgps1.buenosaires.gob.ar', 'bienes.buenosaires.gob.ar', 'clipping.buenosaires.gob.ar', 'formularios.buenosaires.gob.ar', 'mandatarios.buenosaires.gob.ar', 'moda.buenosaires.gob.ar', 'rondaeditorial.buenosaires.gob.ar', 'cmct.buenosaires.gob.ar', 'cmctgps2.buenosaires.gob.ar', 'datosestudiantes.buenosaires.gob.ar', 'expresometro.buenosaires.gob.ar', 'serviciobicicletas.buenosaires.gob.ar', 'bibliotecateatrocolon.buenosaires.gob.ar', 'baset.buenosaires.gob.ar', 'estatico-boletines.buenosaires.gob.ar', 'blogs.buenosaires.gob.ar', 'mapa1.buenosaires.gob.ar', 'rs1.buenosaires.gob.ar', 'estatico.buenosaires.gob.ar', 'pdsl.buenosaires.gob.ar', 'prrac2.buenosaires.gob.ar', 'acceder.buenosaires.gob.ar', 'escueladomi1media.buenosaires.gob.ar', 'feriadelibrovirtual.buenosaires.gob.ar', 'indexer.webbeta.buenosaires.gob.ar', 'notificaciones.buenosaires.gob.ar', 'palermolimpio.buenosaires.gob.ar', 'searcher.webbeta.buenosaires.gob.ar', 'telesalud.buenosaires.gob.ar', 'tgplaneamiento.buenosaires.gob.ar', 'veranociudad.buenosaires.gob.ar', 'webbeta.buenosaires.gob.ar', 'sig.buenosaires.gob.ar', 'yoreciclo.buenosaires.gob.ar', 'transparencia.buenosaires.gob.ar', 'pmcaba.buenosaires.gob.ar', 'bicentenariociudad.buenosaires.gob.ar', 'planhidraulico.buenosaires.gob.ar', 'sp.buenosaires.gob.ar', 'haciendoelcolond.buenosaires.gob.ar', 'definitivo.buenosaires.gob.ar', 'festivalem.buenosaires.gob.ar', 'redcomenius.buenosaires.gob.ar', 'tablero.buenosaires.gob.ar', 'bo.buenosaires.gob.ar', 'estatico-resultados-elecciones.buenosaires.gob.ar', 'resultados-elecciones.buenosaires.gob.ar']
#listUrls = ['agip.gob.ar', 'baelige.gob.ar', 'ambadata.gob.ar', 'mibuenosairesweb.gov.ar', 'mibuenosairesweb.gob.ar', 'cedem.gob.ar', 'voluntarios.gob.ar', 'voluntarios.com.ar', 'voluntariosba.com.ar', 'soyvoluntario.com.ar', 'somosvoluntarios.com.ar', 'voluntariosdelaciudad.com.ar', 'voluntarios.net.ar', 'potenciate.gob.ar', 'voluntariosba.gob.ar', 'soyvoluntario.gob.ar', 'somosvoluntarios.gob.ar', 'voluntariosdelaciudad.gob.ar', 'soyvoluntario.net.ar', 'somosvoluntarios.net.ar', 'voluntariosdelaciudad.net.ar', 'voluntariosba.net.ar', 'gobbsas.gov.ar', 'gobbsas.gob.ar', 'vamoslosvecinos.com.ar', 'vamoslosvecinos.net.ar', 'vamoslosvecinos.gob.ar', 'sial.gob.ar', 'sial.gov.ar', 'torchbearer2018.gob.ar', 'ba2018.gob.ar', 'buenosaires2018.gob.ar', 'volunteers2018.gob.ar', 'voluntarios2018.gob.ar', 'metrobus.com.ar', 'codoacodo.gob.ar', 'puntosba.gob.ar', 'planetario.gob.ar', 'ventas-planetario.gob.ar', 'miba.com.ar', 'mdebuenosaires.gob.ar', 'COESS.gob.ar', 'serviciosciudad.gob.ar', 'serviciosciudad.com.ar', 'ciudadabiertatv.gob.ar', 'justiciaenescuelas.gob.ar', 'buenosaires.gob.ar', 'buenosaires.gov.ar', 'buenosairesciudad.gob.ar', 'buenosairesciudad.com.ar', 'vamosbuenosaires.gob.ar', 'oncediez.gob.ar', 'vamosbuenosaires.com.ar', 'hospitalgutierrez.gob.ar', 'defensoria.gob.ar', 'teatrosanmartin.gob.ar', 'plandemovilidad.gob.ar', 'pmetropolitana.gob.ar', 'policia.gob.ar', 'asibuenosaires.org.ar', 'asi.org.ar', 'pmetropolitana.gov.ar', 'cmd.gob.ar', 'policia.gov.ar', 'polmet.gob.ar', 'policiabsas.gob.ar', 'policiagcba.gob.ar', 'metro.gob.ar', 'baset.gob.ar', 'asibsasdigital.org.ar', 'metrobus.gob.ar', 'agradeselfie.com.ar', 'teatrocolon.gob.ar', 'bafici.gov.ar', 'durandoyg.org.ar', 'la2x4gob.ar', 'agradeselfie.gob.ar', 'parquedelamemoria.org.ar', 'asi.gob.ar', 'buenosairesdigital.gob.ar', 'eleccionesgcba.gob.ar', 'infanciayderechos.gob.ar', 'buenosairescompras.gov.ar', 'saliseguro.gob.ar', 'durand.org.ar', 'buenosairescompras.gob.ar', 'laciudadcompras.gob.ar', 'bafici.gob.ar', 'usig.gob.ar', 'maternidadsarda.gob.ar', 'bac.gob.ar', 'hospitalalgerich.org.ar', 'complejoteatral.gob.ar', 'redexpreso.gob.ar', 'ciudad.gob.ar', 'agenciaambiental.gob.ar', 'zooterapia.gob.ar', 'lanochedelosmuseos.gob.ar', 'enfermeria.gob.ar', 'same.gov.ar', 'same.gob.ar', 'hospitalalvear.gov.ar', 'hospitalalvear.gob.ar', 'ciudademergente.gob.ar', 'badesdeadentro.gob.ar', 'pig.gob.ar', 'dengue.gob.ar', '2019elecciones.gob.ar', 'gcbanotributarios.gob.ar', 'gcbanotributarios.gov.ar', 'ciudadanIaglobal.com.ar', 'buenosairesjazz.gob.ar', 'buenosairesjazz.gov.ar', 'generacionba.gob.ar', 'bibleduc.gob.ar', 'mhnotributarios.gob.ar', 'mhnotributarios.gov.ar', 'centroameghino.gob.ar', 'ba.gob.ar', 'ba.gov.ar', 'bsas.gob.ar', 'bsas.gov.ar', 'hospitalsantojanni.gov.ar', 'hospitalsantojanni.gob.ar', 'oncediez.com.ar', 'elizalde.gob.ar', 'gcba.gov.ar', 'gcba.gob.ar', 'defensacivil.gob.ar', 'defensacivil.gov.ar', 'registrocivil.gob.ar', 'gripea.gob.ar', 'disfrutemosba.com.ar', 'bacapitalgastronomica.com.ar', 'la2x4.com.ar', 'jugalimpio.gob.ar', 'escuelasverdes.gob.ar', 'bsasmail.gob.ar', 'miba.gob.ar', 'treintaytodos.com.ar', 'hospitaldurand.org.ar', 'dguiaf-gcba.gob.ar', 'dguiaf-gcba.gov.ar', 'prensagcba.com.ar', 'innovaires.gob.ar', 'ba-csirt.gob.ar', 'disfrutemosba.gob.ar', 'treintaytodos.gob.ar', 'medueleunateta.com.ar', 'comoprevenirelcancerdemama.com.ar', 'tengounamanchaenlamama.com.ar', 'tengounamanchaenlamama.com.ar', 'sientounapuntadaenunateta.com.ar', 'tengoalgoraroenelpezon.com.ar', 'tengounatetaroja.com.ar', 'sientoardorenunamama.com.ar', 'tengoinflamadounseno.com.ar', 'tengounamamahinchada.com.ar', 'tengounnoduloenelpecho.com.ar', 'tengoelpezonhundido.com.ar', 'tengounabolitaenelpecho.com.ar', 'tengounbultoenlateta.com.ar', 'tratamientoparaelcancerdemama.com.ar', 'sintomasdelcancerdemama.com.ar', 'tengocancerdemama.com.ar', 'internetnoesmedico.com.ar', 'agendacultural.gob.ar', 'sindicaturagcba.gob.ar', 'bafc.gob.ar', 'jardinbotanico.gob.ar', 'reservaecologica.gob.ar', 'comosesiunbultoenlatetaesmaligno.com.ar', 'irep.gob.ar', 'bibliotecas.gob.ar', 'bacapitalgastronomica.gob.ar', 'guti.gob.ar', 'buenosaires2020.gob.ar', 'filacero.com.ar', 'filacero.gob.ar', 'festivales.gov.ar', 'tangobuenosaires.gob.ar', 'estacionamiento.gob.ar', 'bamascotas.gob.ar', 'institutomemoria.org.ar', 'metropolitana.gov.ar', 'metropolitana.gob.ar', 'puntosba.gob.ar', 'alquilerba.gob.ar', 'agcontrol.gov.ar', 'agcontrol.gob.ar', 'hospital-muniz.org.ar', 'baelige.net.ar', 'buenosaireselige.net.ar', 'buenosaireselige.com.ar', 'registrocivil.com.ar', 'investba.gob.ar', 'inversionesba.gob.ar', 'festivales.gob.ar', 'hospitalmuniz.gob.ar', 'hospital-muniz.gob.ar', 'buenosairesemprende.gob.ar', 'bue.gob.ar', 'bue.gov.ar', 'ccgsm.gob.ar', 'turismocultural.gob.ar', 'museoquinquela.gob.ar', 'airesbuenosaires.gob.ar', 'baelige.com.ar', 'policiadelaciudad.gob.ar', 'insusep.edu.ar']
#Nombre del Archivo a guardar
fileName = 'pasadaCompletaExternos_conVPN.txt'

#Encabezado del Archivo de texto
header = 'Lista URLS: Pasada Completa Externos - Con VPN'

#VPN = Valores conVpn o sinVpn
vpn = 'conVpn'

count = 0
#de 210


def getWebImg(url, counter, prefix):
    options = webdriver.FirefoxOptions
    options.headless = False
    options.accept_insecure_certs = True
    driver = webdriver.Firefox(executable_path=r'/Utils/geckodriver.exe')
    driver.get('http://' + url)
    time.sleep(1)
    print("tomando captura de " + str(counter +1 ) + " " + url)
    nameString1 = url.replace('.', '-')
    nameString = nameString1.replace('/', '-')
    try:
        driver.get_screenshot_as_file('/ProcesosTemp/' + str(counter + 1) + "-" + vpn + "-" + prefix + nameString + '_screenshot.png')
    except:
        print("pasando de largo")
    finally:
        driver.quit()
    print("end...")

def procesoURL(prefix, url, counter, respuesta):
    try:
        w = whois.whois(url)
    except whois.parser.PywhoisError as e:
        w = str(e)

    print("\n"+ str(counter + 1) + " - " + prefix + url + "\nRespuesta Servidor: " + respuesta + "\nTimeStamp: " + str(datetime.now()) + "\nInforme Dominio: " + str(w))
    print("\n"+ str(counter + 1) + " - " + prefix + url + "\nRespuesta Servidor: " + respuesta + "\nTimeStamp: " + str(datetime.now()) + "\nInforme Dominio: " + str(w), file=f)

with open(fileName, 'w') as f:
    print(header, file=f)
    for each in listUrls:
        try:
            response, content = h.request('http://' + listUrls[count])
            procesoURL("http://", listUrls[count], count, str(response.status))
            getWebImg(listUrls[count], count, "")

        except httplib2.ServerNotFoundError:
            procesoURL("http://", listUrls[count], count, "SERVER NOT FOUND ERROR")
            getWebImg(listUrls[count], count, "")

        except (httplib2.HttpLib2Error, socket.error) as ex:
            procesoURL("http://", listUrls[count], count, "TIMEOUT ERROR")
            getWebImg(listUrls[count], count, "")

        try:
            response, content = h.request('http://www.' + listUrls[count])
            procesoURL("http://www.", listUrls[count], count, str(response.status))
            getWebImg(listUrls[count], count, "www-")

        except httplib2.ServerNotFoundError:
            procesoURL("http://www.", listUrls[count], count, "SERVER NOT FOUND ERROR")
            getWebImg(listUrls[count], count, "www-")

        except (httplib2.HttpLib2Error, socket.error) as ex:
            procesoURL("http://", listUrls[count], count, "TIMEOUT ERROR")
            getWebImg(listUrls[count], count, "www-")

        count = count + 1

