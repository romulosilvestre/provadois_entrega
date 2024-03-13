import pandas as pd
from collections import Counter


class SkillList:
    def __init__(self):
        pass

    def skill_one(self):
        print("Uma classe é uma coleção de objetos")
        print("O objeto é uma instância de uma classe")
        print("Na classe declaramos construtor e métodos get e set")
        print("Na classe criamos métodos concretos e abstratos")
        print("Na classe criamos métodos workers (de trabalho)")
        print("Na classe podemos criar modelos usando ferramentas de ORM")
        print("Na classe podemos implementar CRUDs")
        print("Na classe podemos criar cálculos e implementar RNs (BO)")

    def skill_two(self):
        print("A função principal main é usada para executar o programa")
        print("É a partir dela que podemos importar outros pacotes")
        print("Nela podemos criar objetos de diversas classes")

    def skill_three(self):
        # Podemos rastrear erros e bugs
        # "Um erro de sintaxe é sinalizado na ferramenta"
        # Um erro lógico pode ter sua solução com a ferramenta debug."
        # Importante aprender sobre breakpoint!"
        print("Coloque para debugar e use F8 para pular para a próxima linha do debug")

    def skill_four(self):
        # Importe o pandas lá no inicio da classe"
        # Caso não tenha instalado abra o terminal e digite: pip install pandas
        # Use um apedido pd
        # Prepare o arquivo e coloque-o no diretório
        # Vamos começar usar o Pandas
        # Pandas é, talvez, a biblioteca de manipulação de dados mais utilizada pelos programadores
        # Funciona como uma camada de abstração sobre NumPy
        # NumPy é uma biblioteca que facilita a realização de cálculos cientificos.
        # Outra biblioteca é a Scikit-Learn, mas para IA (Inteligência Aritificial)
        # Vamos começar carregando um arquivo com Pandas.
        # Primeiro temos que instância um objeto
        # Esse objeto é um objeto Pandas
        # Internamente esse objeto é chamado de DataFrame
        # Assim podemos utilizar funções poderosas
        # Funções de leitura e tratamento de dados
        # Vamos utilizar um arquivo com a extensão csv
        # csv significa comma-separated-values
        # valores separados por vírgulas
        # abra o arquivo e estude o arquivo.
        # os arquivos csv geralmente declaram as colunas em sua primeira linha
        # A biblioteca pandas tem várias funções
        # Mas precisamos carregar primeiro os dados
        # Você já importou?
        # então vamos fazer a carga.
        # dataframe = pd.read_csv("nome do arquivo")
        # o nome pd se tornou regra , mas não é obrigatório
        # Series e DataFrames...
        # FIXME:carregar dados do tipo csv
        dataframe = pd.read_csv("properties.csv")


    def skill_five(self):
        pass
        # Um dicionário é um tipo de dados de Python que agrupa atributos
        # Esse agrupamento é por meio de identificadores, comumente referidos como "etiquetas"
        # (labels) - são essas etiquetas
        # Ela funciona como um array associativo, presente, por exemplo, no php
        # Assim ele cria uma correspondência entre chaves e valores.
        """
          exemplo de dicionário
        """
        clientes = {}  # criando dicionário vazio (preferida pelos pythônicos)
        funcionario = dict()  # criando dicionário vazio
        pesos = {'Rômulo': 105.00, 'Raimundo': 77.56}  # As chaves são os nomes e os valores o peso
        # O comum é que as chaves sejam strings
        # Embora pouco usual pode-se utilizar quaisquer outros tipos desde que imutáveis
        # O valor pode ser qualquer um.
        # Os valores precisam ser delimitados por aspas apenas se forem strings
        # Um exemplo abaixo vai mostrar dados de um produto

        product= {
            'code': '00035-B',
            'name': 'Chave de fenda n.15',
            'price': 29.759}

        print("Printing all product content")
        print(product)
        print("Printing the product type")
        print(type(product))
        print("Printing the product code")
        print(product['code'])
        print("Printing the product name")
        print(product['name'])
        print("Printing the product price")
        print(f"$ {product['price']:.2f}")
        #Uma variável do tipo dicionário não pode conter chaves repetidas.
        #A classe Counter é bem interessante
        #Uma classe muito útil em programas relacionados a estatística é Counter (contador)
        #Ela permite implementar facilmente uma distribuição de frequência
        #Um Counter é uma coleção sem ordenação
        #No qual os itens são armazenados como chaves
        #Chaves de um dicionários e os valores correspondem à frequência
        #Quantidade de vezes em que aparece na amostra dos elementos da coleção
        #Você deve importar: from collections import Counter
        lista_numeros = [0,1,2,2,1,2,0]
        c1 = Counter(lista_numeros)
        print(f"lista de números: {lista_numeros}")
        print(f"Distribuição dos números: {c1}")

        #Vamos agora voltar para o nosso desafio.
        #Vamos verificar se esta tudo ok com o campo price que é muito importante.
        product_has_price = 'price' in product
        print("Is the price column ok in the dictionary?")
        print(product_has_price)

        #O que são series e dataframes?
        #As duas principais estruturas de um um objeto Pandas são Series e DataFrames
        #Trocando em miúdos, um objeto Series é um array unidimensional, ou seja, um vetor.
        #Por sua vez, um DataFrame é uma matriz bidimensional rotulada
        #Ou seja, para a qual podem ser atribuídos rotulos (nomes) aos seus atributos (colunas).
        #As melhores series do ENEM
        series_enem = pd.Series([1998,1999,2000,2001])
        print("As melhores series do Enem")
        print(series_enem)
        print("Criando uma série")
        s = pd.Series(['Wes McKinney','Criador do Pandas'],index=['Criador','Tecnologia'])
        print(s)
        print(type(s))
        #FIXME: uso importante de head e tail
        #vamos carregar de novo o dataframe
        dataframe_v2 = pd.read_csv("properties.csv")
        print("head mostra as cinco primeiras entradas")
        print(dataframe_v2.head())
        print("tail mostra as cinco últimas entradas")
        print(dataframe_v2.tail())
        print("Vamos converter um dataframe em um dicionário")
        dicio = dataframe_v2.to_dict()
        print("Dicionário")
        print(dicio)
        print(type(dicio))
    def skill_six(self):
        dataframe_v3 = pd.read_csv("properties.csv")
        qtde = len(dataframe_v3)
        print(f"quantidade de registros:{qtde}")



