from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/Users/marle/OneDrive/Documentos/infovid/utils/chromedriver')
driver.get("https://news.google.com/covid19/map?hl=pt-BR&mid=%2Fm%2F015fr&gl=BR&ceid=BR%3Apt-419")

lugares_brutos = driver.find_elements_by_class_name('pcAJd')
dados_brutos = driver.find_elements_by_css_selector('td.l3HOY')

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

# for i in range(27):
#     print(i+1, ' - ', pegar_informacoes(i).split(";"))

driver.quit()

