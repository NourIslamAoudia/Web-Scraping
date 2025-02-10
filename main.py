import requests
import csv
from bs4 import BeautifulSoup

# Demande à l'utilisateur de saisir la date
date = "2/11/2025"

# Effectuer la requête HTTP
url = f'https://www.yallakora.com/match-center?date={date}'
response = requests.get(url)

# Vérifier si la requête a réussi
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'lxml')
    
    # Trouver toutes les cartes de match
    matches = soup.find_all('div', class_='matchCard')
    teams=[]
    
    for match in matches:
        data = match.find_all('div', class_='allData')
        for d in data:
            teamsdatas= d.find_all('div', class_='teamsData')
            for t in teamsdatas:
                team= t.find('p').text
                teams.append(team)


    


# Write to HTML file
with open('output.html', 'w', encoding='utf-8') as file:
    for data in teams:
        file.write(data)
        file.write('\n')