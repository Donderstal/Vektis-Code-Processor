from bs4 import BeautifulSoup
from urllib.request import urlopen

import json
import gegevensElementen
import standaarden
import codeLijsten

def getGegevensElementen( test = False ):
    Gegevens_Elementen = getSideBarList('https://www.vektis.nl/standaardisatie/gegevenselementen')
    Gegevens_Elementen_Data = []

    print(len(Gegevens_Elementen))
    index = 0

    if test == True:
        gegevensElementen.addGegevensElement(Gegevens_Elementen_Data, Gegevens_Elementen[0])
        print('elementen')
        print(Gegevens_Elementen_Data)
    
    else:
        for Element in Gegevens_Elementen:
            gegevensElementen.addGegevensElement(Gegevens_Elementen_Data, Element)
            index += 1
            print(index)

        with open('gegevens_elementen.json', 'w') as json_file:
            json.dump(Gegevens_Elementen_Data, json_file)

def getCodeLijsten( test = False ):
    Code_Lijsten = getSideBarList('https://www.vektis.nl/standaardisatie/codelijsten')
    Code_Lijsten_Data = []

    print(len(Code_Lijsten))
    index = 0

    if test == True:
        codeLijsten.addCodeLijst(Code_Lijsten_Data, Code_Lijsten[0])
        print('codelijsten')
        print(Code_Lijsten_Data)

    else:
        for Element in Code_Lijsten:
            codeLijsten.addCodeLijst(Code_Lijsten_Data, Element)
            index += 1
            print(index)

        with open('code_lijsten.json', 'w') as json_file:
            json.dump(Code_Lijsten_Data, json_file)

def getStandaarden( test = False ):
    Standaarden = getSideBarList('https://www.vektis.nl/standaardisatie/standaarden')
    Standaarden_Data = []

    print(len(Standaarden))
    index = 0

    if test == True:
        standaarden.addStandaard(Standaarden_Data, Standaarden[0])
        print('standaard')
        print(Standaarden_Data)

    else:
        for Element in Standaarden:
            standaarden.addStandaard(Standaarden_Data, Element)
            index += 1
            print(index)

        with open('standaarden.json', 'w') as json_file:
            json.dump(Standaarden_Data, json_file)

def getSideBarList(url):
    Pagina = BeautifulSoup( urlopen(url).read() )
    return Pagina.findAll("ul", {"class": "standards"})[0].findAll("li", {"class": "standards__item"})

def getAll():
    test = True
    getStandaarden(test)
    getCodeLijsten(test)
    getGegevensElementen(test)

getAll()