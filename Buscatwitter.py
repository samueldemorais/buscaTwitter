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
        return tabela_data

    def BuscaTermo(self, termo:str):
        tabela['termo'] = tabela.content.str.contains(termo)
        tabela_data = tabela.query("termo==True")[['date', 'content', 'subject']]
        return tabela_data

    def BuscaAssunto(self, assunto:str):
        tabela['assunto'] = tabela.subject.str.contains(assunto)
        tabela_data = tabela.query("assunto==True")[['date', 'content', 'subject']]
        return tabela_data

def main():
    twitter = Busca()
    print('''Boas vindas ao nosso sistema:

1 - Buscar tweets por data
2 - Buscar tweets por termo
3 - Buscar tweets por assunto
4 - Salvar resultado da busca
5 - Sair''') 
    while True:
       comando = int(input('\n>>> '))
       if comando == 5:
        break
       elif comando == 1:
        data = str(input('Digite a data no formato dd/mm/aaa:'))
        print(twitter.BuscaData(data))
       elif comando == 2:
        termo = str(input('Digite o termo que você quer procurar:'))
        print(twitter.BuscaTermo(termo))
       elif comando == 3:
        print("assuntos disponíveis: 1. Copa do Mundo 2. Eleições 3. Ciência de Dados 4. COVID-19")
        newcomando = int(input('digite o número correspondente ao assunto que você quer buscar>>> '))
        if newcomando == 1:
            print(twitter.BuscaAssunto('copa do mundo'))
        elif newcomando ==2: 
            print(twitter.BuscaAssunto('eleições'))
        elif newcomando ==3: 
            print(twitter.BuscaAssunto('ciência de dados'))
        elif newcomando == 4:
            print(twitter.BuscaAssunto('covid-19'))
            

       


if __name__ == "__main__":
    main()