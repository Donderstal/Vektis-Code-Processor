from bs4 import BeautifulSoup
from urllib.request import urlopen

def addGegevensElement(Gegevens_Elementen_Data, Element):
    ElementUrl = Element.find('a')['href']

    ElementPage = BeautifulSoup( urlopen(ElementUrl).read() )

    dictionaryEntry = {'Standaarden': []}

    IdSection = ElementPage.find('section', { "id": "identificatie" }).find("div", {"class": "component__content"}).findAll("p")

    for i in IdSection:
        dictionaryKey = i.find('b').getText().strip()
        i.find('b').decompose()
        i.find('br').decompose()
        dictionaryEntry[dictionaryKey] = i.getText().strip()

    CodeContentSection = ElementPage.find('section', { "id": "codering" }).find("div", {"class": "component__content"}).findAll("div", {"class": "col-sm-3"})

    for c in CodeContentSection:
        paragraph = c.find("p")
        dictionaryKey = paragraph.find('b').getText().strip()

        paragraph.find('a').decompose()
        paragraph.find('b').decompose()
        paragraph.find('br').decompose()
        dictionaryEntry[dictionaryKey] = paragraph.getText().strip()

    UsedInStandardSection = ElementPage.find('section', { "id": "gebruik" }).find("div", {"class": "component__content"})
    UsedInStandardKeys  = UsedInStandardSection.find("thead").findAll("th")
    UsedInStandardValues = UsedInStandardSection.find("tbody").findAll("tr")

    for u in UsedInStandardValues:
        Standard = {}
        Type = u.find("td").find("a")
        Standard[UsedInStandardKeys[0].getText()] = Type.getText().replace('\n', '').replace(' ', '').replace('versie', '').strip()
        Standard[UsedInStandardKeys[1].getText()] = u.findAll("td")[1].getText().strip()
        Standard[UsedInStandardKeys[2].getText()] = u.findAll("td")[2].getText().strip()
        dictionaryEntry['Standaarden'].append(Standard)

    Gegevens_Elementen_Data.append(dictionaryEntry)