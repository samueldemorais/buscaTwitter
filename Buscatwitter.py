import pandas as pd
from IPython.display import display

tabela = pd.read_csv("Bancotweets.csv", sep=';')
tabela_datas = []
corta_data = tabela['date'].str.split(' ', n=1, expand= True)
tabela['date'] = corta_data[0]
tabela['time'] = corta_data[1]
#display(tabela.head())
#data = tabela[tabela.date == "17/10/2022 03:42"]
#linha = tabela.loc[linhas, colunas]
#print(linha)

#print(data)

class Busca:

    def __init__(self) -> None:
        pass

    def BuscaData(self, Data:str):
        tabela['data'] = tabela.date.str.contains(Data)
        tabela_data = tabela.query("data==True")[['date', 'content', 'subject']]
        print(tabela_data)

    def BuscaTermo(self, termo:str):
        tabela['termo'] = tabela.content.str.contains(termo)
        tabela_data = tabela.query("termo==True")[['date', 'content', 'subject']]
        print(tabela_data)

    def BuscaAssunto(self, assunto:str):
        tabela['assunto'] = tabela.subject.str.contains(assunto)
        tabela_data = tabela.query("assunto==True")[['date', 'content', 'subject']]
        print(tabela_data)

if __name__ == "__main__":
    twiiter = Busca()
    twiiter.BuscaAssunto("ciência de dados")