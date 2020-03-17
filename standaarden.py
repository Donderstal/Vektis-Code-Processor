from bs4 import BeautifulSoup
from urllib.request import urlopen

baseRowId = 'collapsed-table__row--'

def addStandaard(Standaard_Data, Element):
    ElementUrl = Element.find('a')['href']

    ElementPage = BeautifulSoup( urlopen(ElementUrl).read() )

    dictionaryEntry = {'Berichtstructuur': []}

    IdSection = ElementPage.find('section', { "id": "identificatie" }).find("div", {"class": "component__content"}).findAll("p")
    getIdSection(IdSection, dictionaryEntry)

    StructureSection = ElementPage.find('section', { "id": "berichtstructuur" }).find("div", {"class": "component__content"}).findAll("a")
    getUsedInStandardsSection(StructureSection, dictionaryEntry, ElementPage)

    Standaard_Data.append(dictionaryEntry)

def getIdSection(IdSection, dictionaryEntry):
    for i in IdSection:
        dictionaryKey = i.find('b').getText().strip()
        i.find('b').decompose()
        i.find('br').decompose()
        dictionaryEntry[dictionaryKey] = i.getText().strip()

def getUsedInStandardsSection(StructureSection, dictionaryEntry, ElementPage):
    for a in StructureSection:
        headers = []

        dataCode    = a['data-code']
        lineCode    = a.find("div", {"class": "msg-structur__code"})
        lineLabel   = a.find("div", {"class": "msg-structur__label"})

        if ElementPage.find('tr', { "class": baseRowId + dataCode }) != None:
            lineHeaders = ElementPage.find('tr', { "class": baseRowId + dataCode }).findAll("th")

            for header in lineHeaders:
                if header.getText() != '':
                    headers.append(header.getText())

            ElementPage.find('tr', { "class": baseRowId + dataCode }).decompose()
        dictionaryEntry['Berichtstructuur'].append(getLineInformation(dataCode, ElementPage, headers, dictionaryEntry))

    print(dictionaryEntry)

def getLineInformation(dataCode, ElementPage, headers, dictionaryEntry):
    lineRows = ElementPage.findAll('tr', { "class": baseRowId + dataCode })
    cellContent = []
    returnArray = [{}]

    for row in lineRows:
        returnDict = {}
        rowCells = row.findAll("td")
        cellContent = getCellContents(rowCells)
        index = 0

        while index < len(headers):
            returnDict[headers[index]] = cellContent[index]
            index += 1
        
        returnArray.append(returnDict)

    return returnArray

def getCellContents(rowCells):
    i = 0
    cellContent = []

    for cell in rowCells:
        if i == 2:
            i += 1
            continue
        cellContent.append(cell.getText().strip())
        i += 1
        
    return cellContent
