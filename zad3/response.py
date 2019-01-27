#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import sys
import os
import validators

class MyCustomException(Exception):
        pass

def check_parameters_count(arrgs):
#Funkcja sprawdza ilość parametrów w wywołaniu.
#Gdy różna od 2 wywołuje Exception
    if len (arrgs) < 2:
       raise MyCustomException('No parameters! Please provide URL')
    elif len (arrgs) > 2:
       raise MyCustomException("To many parameters!")
    
def checkurl(url):
#Funkcja sprawdza poprawność adresu URL
#Jeżeli nie jest poprawne, wywołuje Exception
    if not validators.url(url):
        raise MyCustomException('URL is not valid')
    
def getResonse(address):
#Funkcja odpytuje api. 
#Jeżeli nie odstanie odpowiedzi przez 10s. wywoła Exception
#Zwraca status otrzymany od aplikacji.
    try:
        response = requests.get(address, timeout=10)
        return response.status_code
    except requests.exceptions.RequestException:
       raise MyCustomException('Timeout')


def main():

    #Sprawdź czy plik z pidem istnieje, jeżeli tak, nie pozwól na uruchomienie.
    #Jeżeli nie istnieje, utwórz pid i przejdź dalej.
    pid = str(os.getpid())
    pidfile = "./get_response_from_app.pid"
    if os.path.isfile(pidfile):
        print ("PID file: %s exists. another instance is running." % pidfile)
        sys.exit()
    open(pidfile, 'w').write(pid)

    try:
        check_parameters_count(sys.argv)
        url=sys.argv[1]
        checkurl(url)
        e = getResonse(url)
   
        if e == 201:
            print("OK!")
            sys.exit(0)
        else:
            print("FAIL")
            sys.exit(1)

    except MyCustomException as ex:
        print(ex)
        sys.exit (1)

    finally:
        #skasuj pid
        os.unlink(pidfile)



if __name__ == '__main__':
    main()