#Entrega Final: Análise da quantidades de reclamações para cada faixa etária.
#Nome: Pedro Ricardo 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Função ler a base de dados em arquivo csv, sep (retira o ; para realizar a leitura correta) e chama a função (dadosNomeEmpresa).
def dadosCSV():
    dados = pd.read_csv('base.csv', sep=';')
    dadosNomeEmpresa(dados)

# A função recebe como parâmetro os dados do arquivo csv e itera adicionando dentro de um array a faixa etária da empresa 'Facebook / Instagram'
#Após finalizar a iteração chama a função (dadosFaixaEtaria)
def dadosNomeEmpresa(dados):
    fb = []
    for i in range(len(dados)):
        if i != 0 and dados['Nome Fantasia'][i] == 'Facebook / Instagram':
            fb.append(dados['Faixa Etária'][i])
    dadosFaixaEtaria(fb)

#A função recebe como parâmetro o array com os dados da faixa etária e faz a contagem de cada faixa etária correspondente e depois chama a função grafico.
def dadosFaixaEtaria(fb):
    faixaEtaria = {}
    for faixa in fb:
        if faixa in faixaEtaria:
            faixaEtaria[faixa] += 1
        else:
            faixaEtaria[faixa] = 1
    grafico(faixaEtaria)

#Essa função faz o plot do gráfico contendo as informações com a contagem de cada faixa etária e o nomes.
def grafico(faixaEtaria):
    faixas = list(faixaEtaria.keys())
    contagens = list(faixaEtaria.values())

    plt.figure(figsize=(10, 6))
    plt.bar(faixas, contagens)
    plt.xlabel('Faixa Etária')
    plt.ylabel('Contagem')
    plt.title('Contagem para cada Faixas Etárias para Facebook / Instagram')
    plt.xticks(rotation=45)
    plt.tight_layout()

    for i, contagem in enumerate(contagens):
        plt.text(i, contagem + 0.1, str(contagem), ha='center', va='bottom')

    plt.show()

dados = dadosCSV()