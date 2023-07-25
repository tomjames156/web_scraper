import requests
from bs4 import BeautifulSoup
from languages import get_languages_sentence

response = requests.get('https://tomis-portfolio.netlify.app/')
portfolio_soup = BeautifulSoup(response.text, 'html.parser')
my_projects = portfolio_soup.find_all("div", "project-name")
languages_container = portfolio_soup.find_all('div', 'languages')

for project, language_container in zip(my_projects, languages_container):
    print(f"{project.string} built with {get_languages_sentence(str(language_container))}")
    
# special_soup = <p>Yo Pierre you wanna come <span style="text-decoration: underline;">out</span> <strong>here</strong>?</p>