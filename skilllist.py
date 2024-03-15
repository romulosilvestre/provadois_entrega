import time
import pandas as pd
from collections import Counter
from colorama import Fore
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


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

        product = {
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
        # Uma variável do tipo dicionário não pode conter chaves repetidas.
        # A classe Counter é bem interessante
        # Uma classe muito útil em programas relacionados a estatística é Counter (contador)
        # Ela permite implementar facilmente uma distribuição de frequência
        # Um Counter é uma coleção sem ordenação
        # No qual os itens são armazenados como chaves
        # Chaves de um dicionários e os valores correspondem à frequência
        # Quantidade de vezes em que aparece na amostra dos elementos da coleção
        # Você deve importar: from collections import Counter
        lista_numeros = [0, 1, 2, 2, 1, 2, 0]
        c1 = Counter(lista_numeros)
        print(f"lista de números: {lista_numeros}")
        print(f"Distribuição dos números: {c1}")

        # Vamos agora voltar para o nosso desafio.
        # Vamos verificar se esta tudo ok com o campo price que é muito importante.
        product_has_price = 'price' in product
        print("Is the price column ok in the dictionary?")
        print(product_has_price)

        # O que são series e dataframes?
        # As duas principais estruturas de um um objeto Pandas são Series e DataFrames
        # Trocando em miúdos, um objeto Series é um array unidimensional, ou seja, um vetor.
        # Por sua vez, um DataFrame é uma matriz bidimensional rotulada
        # Ou seja, para a qual podem ser atribuídos rotulos (nomes) aos seus atributos (colunas).
        # As melhores series do ENEM
        series_enem = pd.Series([1998, 1999, 2000, 2001])
        print("As melhores series do Enem")
        print(series_enem)
        print("Criando uma série")
        s = pd.Series(['Wes McKinney', 'Criador do Pandas'], index=['Criador', 'Tecnologia'])
        print(s)
        print(type(s))
        # FIXME: uso importante de head e tail
        # vamos carregar de novo o dataframe
        dataframe_v2 = pd.read_csv("properties.csv")
        print("head mostra as cinco primeiras entradas")
        print(dataframe_v2.head())
        print("tail mostra as cinco últimas entradas")
        print(dataframe_v2.tail())
        print("Vamos converter um dataframe em um dicionário")
        dicio = dataframe_v2.to_dict(orient='records')
        print("Dicionário")
        print(dicio)
        print(type(dicio))

    def skill_six(self):
        dataframe_v3 = pd.read_csv("properties.csv")
        qtde = len(dataframe_v3)
        print(f"quantidade de registros:{qtde}")

    def skill_seven(self):
        """
         Função para analisar registros de um arquivo CSV chamado "properties.csv".
         """
        print("Analisando os registros:")
        dataframe_v4 = pd.read_csv("properties.csv")
        dicio2 = dataframe_v4.to_dict(orient='records')
        for indice, registro in enumerate(dicio2):
            print(f"Registro {indice}:")
            for chave, valor in registro.items():
                print(f"{chave}: {valor}")
            print(f"{Fore.RED}*****************************************************{Fore.RESET}")
        #um outro recurso interessante
        print(f"{Fore.BLUE}imprimindo dtypes{Fore.RESET}")
        print(dataframe_v4.dtypes)
        print(f"{Fore.GREEN}imprimindo describe{Fore.RESET}")
        print(dataframe_v4.describe())
        print(f"{Fore.CYAN}mostrando o campo price{Fore.RESET}")
        print(dataframe_v4['price'])
        print(f"{Fore.RED}mostrando um intervalo do campo price{Fore.RESET}")
        print(dataframe_v4[100:120])
        #estudar fatiar com número negativo pag. 7.16
        #funções iloc( ) e loc( )
        print("mostrando com índice negativo.544-490:54")
        print(dataframe_v4[:-490])
        #buscando usando iloc: é usada para buscar itens unicamente a partir de números inteiros, pelo índice.
        #Vale lembrar aqui que os índices começam com zero e o último
        #item não é incluido então esse item de um dataframe é n-1(número de itens do dataframe -1)
        print("Buscando no índice 3")
        print(dataframe_v4.loc[3])
    def skill_eight(self):
       # Carregar o arquivo CSV em um DataFrame
        dataframe_v5 = pd.read_csv("properties.csv")
        print("mostre o dataframe carregado!")
        # Filtrar as linhas que atendem às condições especificadas
        condicoes = (dataframe_v5['area'] >= 10000) & \
                    (dataframe_v5['area'] <= 10999) & \
                    (dataframe_v5['price'] >= 5000000) & \
                    (dataframe_v5['price'] <= 5999999) & \
                    (dataframe_v5['bedrooms'] > 2)

        # Obter o índice das linhas que atendem às condições
        indices = condicoes.loc[condicoes].index

        # Executar a linha seguinte para cada índice obtido
        for indice in indices:
            proxima_linha = dataframe_v5.iloc[indice + 1]
            # Aqui você pode fazer o que quiser com a próxima linha, por exemplo, imprimir:
            print("Próxima linha após o índice", indice, ":\n", proxima_linha,"\n")
        op = input("deseja visualizar formatada?")
        if(op == "sim"):
           print("Iremos chamar agora a Skill Nine")
           time.sleep(5)
           self.skill_nine(dataframe_v5)
        else:
            print("finalizado com sucesso!")
    def skill_nine(self,dataframe):

            """
            Função para exibir propriedades filtradas com base em critérios específicos.
            """
            # Definir as condições para filtragem
            condicoes = (dataframe['area'].between(10000, 10999)) & \
                        (dataframe['price'].between(5000000, 5999999)) & \
                        (dataframe['bedrooms'] > 2)

            # Aplicar os filtros
            propriedades_filtradas = dataframe.loc[condicoes]

            # Verificar se existem propriedades filtradas
            if propriedades_filtradas.empty:
                print("Não foram encontradas propriedades que atendam aos critérios.")
            else:
                print("Propriedades que atendem aos critérios:")
                # Exibir as propriedades formatadas
                for indice, propriedade in propriedades_filtradas.iterrows():
                    print(f"Propriedade {indice}:")
                    for coluna, valor in propriedade.items():
                        print(f"{coluna.capitalize()}: {valor}")
                    print("-" * 30)
            print("chamando a skill 12")
            self.skill_twelve(propriedades_filtradas)



    def skill_ten(self):
        # Diretório raiz do projeto
        diretorio_raiz = os.getcwd()

        # Pasta onde estão os arquivos
        pasta_arquivos = os.path.join(diretorio_raiz, 'arquivos')

        # Lista os arquivos na pasta
        arquivos = os.listdir(pasta_arquivos)

        if arquivos:
            # Configurações do servidor SMTP do Gmail
            smtp_server = 'smtp.gmail.com'
            smtp_port = 587  # Porta TLS padrão para o Gmail

            remetente = 'romulogurgeldf@gmail.com'
            senha = 'fodbbsphuvcqmzuh '
            destinatario = 'consultreds@gmail.com'
            assunto = 'Enviando arquivos da prova'

            # Criando o objeto MIMEMultipart
            msg = MIMEMultipart()
            msg['From'] = remetente
            msg['To'] = destinatario
            msg['Subject'] = assunto

            # Adicionando os arquivos como anexos
            for arquivo in arquivos:
                caminho_arquivo = os.path.join(pasta_arquivos, arquivo)
                with open(caminho_arquivo, 'rb') as f:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(f.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename= {arquivo}')
                msg.attach(part)

            # Iniciando uma conexão com o servidor SMTP
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()  # Habilitando a criptografia TLS

            # Faça login no servidor SMTP com seu e-mail e senha
            server.login(remetente, senha)

            # Enviando o e-mail
            texto_email = msg.as_string()
            server.sendmail(remetente, destinatario, texto_email)

            # Fechando a conexão com o servidor SMTP
            server.quit()

        else:
            print("Nenhum arquivo encontrado na pasta 'arquivo'.")

    def skill_twelve(self, propriedades_filtradas):
        nome_pasta = "arquivos"
        # Criar a pasta na raiz do projeto
        print("criando a pasta")
        time.sleep(4)
        os.makedirs(nome_pasta, exist_ok=True)
        # Lista de nomes dos arquivos
        time.sleep(3)
        print("Definindo arquivos")
        nomes_arquivos = ["registro1.txt", "registro2.txt", "registro3.txt"]
        print("criando os três arquivos")
        time.sleep(2)
        for i, nome_arquivo in enumerate(nomes_arquivos):
            caminho_arquivo = os.path.join(nome_pasta, nome_arquivo)
            with open(caminho_arquivo,
                      "w") as arquivo:  # Abre o arquivo no modo de escrita, substituindo o conteúdo existente
                indice = propriedades_filtradas.index[i]  # Obtém o índice do registro na lista de registros filtrados
                propriedade = propriedades_filtradas.iloc[i]  # Obtém o registro correspondente
                print(f"Propriedade {indice}:")
                for coluna, valor in propriedade.items():
                    s = f"{coluna.capitalize()}: {valor}"
                    arquivo.write(s)
                    arquivo.write("\n")
                print("-" * 30)

        time.sleep(2)
        print("Pasta e arquivos criados com sucesso.")




