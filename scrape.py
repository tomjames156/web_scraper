import requests
from bs4 import BeautifulSoup
from languages import *
import pprint
import openpyxl

response = requests.get('https://tomis-portfolio.netlify.app/')
portfolio_soup = BeautifulSoup(response.text, 'html.parser')
my_projects = portfolio_soup.find_all("div", "project-name")
languages_container = portfolio_soup.find_all('div', 'languages')

data = []

for project, language_container in zip(my_projects, languages_container):
    print(f"{project.string} built with {get_languages_sentence(str(language_container))}")
    data.append((project.string, get_languages_str(str(language_container))))


data = tuple(data)
pprint.pprint(data)


wb = openpyxl.Workbook()

sheet = wb.active

sheet['A1'] = 'Projects'
sheet['B1'] = 'Languages Used'

for row in data:
    sheet.append(row)

wb.save('portfolio_projects.xlsx')