import json

Gebruikte_Codelijsten       = []
Gebruikte_Gegevenselementen = []

with open ('./processedData/standaarden.json', 'r') as file:
    json_data = json.load(file)

    for entry in json_data:
        for record in entry['Berichtstructuur']:
            for line in record:
                if 'ID gegevens' in line:
                    elementAlreadyPresent = False
                    
                    for element in Gebruikte_Gegevenselementen:
                        if element == line['ID gegevens']:
                            elementAlreadyPresent = True

                    if elementAlreadyPresent == False:
                        Gebruikte_Gegevenselementen.append(line['ID gegevens'])                

                if 'Codelijst' in line:
                    if line['Codelijst'] == "":
                        continue
                    else:
                        elementAlreadyPresent = False
                        for element in Gebruikte_Codelijsten:
                            if element == line['Codelijst']:
                                elementAlreadyPresent = True

                        if elementAlreadyPresent == False:
                            Gebruikte_Codelijsten.append(line['Codelijst'])          
    
    print(Gebruikte_Gegevenselementen)
    print(Gebruikte_Codelijsten)