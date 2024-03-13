import os.path as p  # Importa o módulo 'os.path' para manipulação de caminhos de arquivos.
import datetime as d  # Importa o módulo 'datetime' para trabalhar com datas e horas.

class SkillZero:
    """Classe que contém funções básicas."""

    def __init__(self):
        """Inicializador da classe. Não faz nada no momento."""
        pass

    def info_readme(self, nome_arquivo):
        """
        Obtém informações sobre o arquivo especificado.

        Args:
            nome_arquivo (str): O nome do arquivo.

        Returns:
            datetime: Um objeto de data e hora representando a última modificação do arquivo.
            str: Uma mensagem indicando que o arquivo não foi encontrado.
        """
        if p.exists(nome_arquivo):  # Verifica se o arquivo especificado existe no sistema.
            infor = p.getctime(nome_arquivo)  # Obtém o tempo de criação do arquivo especificado.
            return d.datetime.fromtimestamp(infor)  # Converte o tempo de criação em um objeto de data e hora.

        else:
            return "arquivo não encontrado"  # Retorna uma mensagem se o arquivo não for encontrado.
