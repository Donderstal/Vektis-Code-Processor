import json

Gebruikte_Codelijsten_ID_List       = []
Gebruikte_Gegevenselementen_ID_List = []

with open ('./processedData/standaarden.json', 'r') as file:
    json_data = json.load(file)

    for entry in json_data:
        for record in entry['Berichtstructuur']:
            for line in record:
                if 'ID gegevens' in line:
                    elementAlreadyPresent = False
                    
                    for element in Gebruikte_Gegevenselementen_ID_List:
                        if element == line['ID gegevens']:
                            elementAlreadyPresent = True

                    if elementAlreadyPresent == False:
                        Gebruikte_Gegevenselementen_ID_List.append(line['ID gegevens'])                

                if 'Codelijst' in line:
                    if line['Codelijst'] == "":
                        continue
                    else:
                        elementAlreadyPresent = False
                        for element in Gebruikte_Codelijsten_ID_List:
                            if element == line['Codelijst']:
                                elementAlreadyPresent = True

                        if elementAlreadyPresent == False:
                            Gebruikte_Codelijsten_ID_List.append(line['Codelijst'])          

Gebruikte_Codelijsten       = []

with open ('./fullList/code_lijsten.json', 'r') as file:
    json_data = json.load(file)
    for codelijst in json_data:
        for codeId in Gebruikte_Codelijsten_ID_List:
            if codelijst['ID'] == codeId:
                Gebruikte_Codelijsten.append(codelijst)

with open('./processedData/code_lijsten.json', 'w') as json_file:
        json.dump(Gebruikte_Codelijsten, json_file)

Gebruikte_Gegevenselementen = []

with open ('./fullList/gegevens_elementen.json', 'r') as file:
    json_data = json.load(file)
    for gegElement in json_data:
        for gegevensId in Gebruikte_Gegevenselementen_ID_List:
            if gegElement['ID'] == gegevensId:
                Gebruikte_Gegevenselementen.append(gegElement)

with open('./processedData/gegevens_elementen.json', 'w') as json_file:
        json.dump(Gebruikte_Gegevenselementen, json_file)