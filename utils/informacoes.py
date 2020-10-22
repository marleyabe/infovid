
from selenium import webdriver
import platform
# abre a Google

if platform.system() == 'Linux':
	path = '/home/infovid/infovid/utils/chromedriver'
elif platform.system() == 'Windows':
	path = 'C:/Users/marle/OneDrive/Documentos/infovid/utils/chromedriver.exe'


options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--window-size=1920x1080')

driver = webdriver.Chrome(executable_path=path, chrome_options=options)
driver.get("https://news.google.com/covid19/map?hl=pt-BR&mid=%2Fm%2F015fr&gl=BR&ceid=BR%3Apt-419")

# Puxa do site da Google os Dados Brutos
lugares_brutos = driver.find_elements_by_class_name('pcAJd')
dados_brutos = driver.find_elements_by_css_selector('td.l3HOY')

# listas vazias para receber os dados/nomes
estados = []
casos = []
novos_casos = []
mortes = []

#organiza os estados
for i in range(len(lugares_brutos)):

    if str(lugares_brutos[i].text) != 'Global' and str(lugares_brutos[i].text) != 'Brasil':
        estados.append(lugares_brutos[i].text)


#organiza os dados por estados
for dado in range(len(dados_brutos)):
    if dado > 5 and (dado % 5 == 0):
        casos.append(dados_brutos[dado].text)
        novos_casos.append(dados_brutos[dado+1].text)
        mortes.append(dados_brutos[dado+4].text)


# funcao para organizar informacoes
def pegar_informacoes(indice):
    for i in range(len(estados)):

        return '{0}; {1}; {2}; {3}'.format(estados[indice], casos[indice], mortes[indice], novos_casos[indice])


driver.quit()

