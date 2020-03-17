from bs4 import BeautifulSoup
from urllib.request import urlopen

def addCodeLijst(Code_Lijsten_Data, Element):
    ElementUrl = Element.find('a')['href']

    ElementPage = BeautifulSoup( urlopen(ElementUrl).read() )

    dictionaryEntry = {'Standaarden': []}

    IdSection = ElementPage.find('section', { "id": "identificatie" }).find("div", {"class": "component__content"}).findAll("p")
    getIdSection(IdSection, dictionaryEntry)

    UsedInStandardSection = ElementPage.find('section', { "id": "gebruikt-in-standaarden" }).find("div", {"class": "specs"})
    getUsedInStandardsSection(UsedInStandardSection, dictionaryEntry)

    Code_Lijsten_Data.append(dictionaryEntry)

def getIdSection(IdSection, dictionaryEntry):
    for i in IdSection:
        dictionaryKey = i.find('b').getText().strip()
        i.find('b').decompose()
        i.find('br').decompose()
        dictionaryEntry[dictionaryKey] = i.getText().strip()

def getUsedInStandardsSection(UsedInStandardSection, dictionaryEntry):
    UsedInStandardKeys      = UsedInStandardSection.find("span").findAll("div")
    UsedInStandardValues    = UsedInStandardSection.findAll("a")
    for u in UsedInStandardValues:
        Standard = {}
        Standard[UsedInStandardKeys[0].getText()] = u.find("div", { "class": "specs__code" }).getText().strip()
        Standard[UsedInStandardKeys[1].getText()] = u.find("div", { "class": "specs__label" }).getText().strip()
        dictionaryEntry['Standaarden'].append(Standard)