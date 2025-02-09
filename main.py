import requests
import csv
import lxml
from bs4 import BeautifulSoup

date = input('Enter the date in the format of dd/mm/yyyy: ')

page = requests.get(f'https://www.yallakora.com/match-center?date={date}')
soup = BeautifulSoup(page.content, 'lxml')

matches = soup.find_all('div', class_='matchCard')
teamsdata = []
for match in matches:
    data = match.find_all('div', class_='allData')
    for d in data:
        teamsdatas= d.find_all('div', class_='teamsData')
        teamsdata.extend(teamsdatas)
    


# Write to HTML file
with open('output.html', 'w', encoding='utf-8') as file:
    for data in teamsdata:
        file.write(data.prettify())
        file.write('\n')