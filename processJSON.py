import json

AcceptedIdList = [
    'AP304',
    'AW319',
    'AW33',
    'AW35',
    'AW37',
    'DG301',
    'FZ301',
    'FZ303',
    'GZ311',
    'GZ321',
    'HA304',
    'JW303',
    'JW321',
    'JWMO303',
    'KZ301',
    'MZ301',
    'OS301',
    'PM304',
    'VK301',
    'WDV',
    'WMO301',
    'WMO303',
    'WMO305',
    'WMO307',
    'WMO315',
    'ZH308',
    'ZH310'
]

Gebruikte_Standaarden = []

with open ('./fullList/standaarden.json', 'r') as file:
    json_data = json.load(file)
    for entry in json_data:
        print('entry')
        currentId = entry['ID']
        currentVersion = entry['Versie']
        print(currentId)
        print(currentVersion)

        for standard_id in AcceptedIdList:
            if currentId == standard_id:
                Gebruikte_Standaarden.append(entry)

    with open('./processedData/standaarden.json', 'w') as json_file:
        json.dump(Gebruikte_Standaarden, json_file)