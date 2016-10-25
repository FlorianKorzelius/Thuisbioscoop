import requests
auth_details = ('Jouw API-gebruikersnaam', 'Jouw API-wachtwoord')
api_url = 'http://api.filmtotaal.nl/filmsoptv.xml?apikey=zk9sbrdvztszm9fjfqokprbbim2cqym1&dag=25-10-2016&sorteer=0'
response = requests.get(api_url, auth=auth_details)

with open('filmlijst.xml', 'w') as myXMLFile:
    myXMLFile.write(response.text)


