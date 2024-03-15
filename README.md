# Tutorial: Python e SMTP uma parceria de sucesso!

Este é um tutorial que explora a integração entre Python e o protocolo SMTP (Simple Mail Transfer Protocol) para envio de e-mails. Aqui você aprenderá sobre o funcionamento do SMTP, suas portas e como utilizá-lo para automatizar o envio de e-mails através de scripts Python.

## O que é SMTP?

O SMTP é um protocolo de comunicação usado para enviar e receber e-mails na internet. Ele é responsável por enviar mensagens de e-mail de um servidor para outro e também por encaminhar mensagens de e-mail do cliente de e-mail para um servidor de e-mail.

## Funcionamento do SMTP

O SMTP opera em uma arquitetura cliente-servidor, onde o cliente se comunica com um servidor SMTP para enviar e-mails. O servidor SMTP é responsável por receber as mensagens do cliente, encaminhá-las para o servidor de e-mail de destino e, em seguida, entregá-las à caixa de correio do destinatário.

## Portas e Protocolos

No contexto de redes de computadores, uma porta é um mecanismo usado para identificar diferentes serviços ou processos em um dispositivo conectado a uma rede. O SMTP opera na porta 25, mas também pode operar em outras portas, como a 587 (comumente usada para enviar e-mails de clientes de e-mail para servidores SMTP), e a 465 (para envio seguro de e-mails usando SSL).

## Habilidades Práticas Abordadas no Tutorial

- **Skill 0:** Criar um README.md para o projeto.
- **Skill 1:** Criar classes com funções específicas.
- **Skill 2:** Criar um arquivo main.py para execução.
- **Skill 3:** Tratar erros de programação e debugar o código.
- **Skill 4:** Realizar a leitura do csv com pandas.
- **Skill 5:** Obter os registros como dicionários.
- **Skill 6:** Descobrir o total de registros no csv.
- **Skill 7:** Construir uma automação que faça a leitura de cada registro.
- **Skill 8:** Construir filtros aplicando operadores lógicos executando linha a linha. ()
- **Skill 9:** Pesquisar colunas e formatar textos para exibição com filtros.
- **Skill 10:** Enviar e-mails aplicando recursos de bibliotecas Python para SMTP.
- **Skill 11:** Elaborar documentação das classes com o uso de docstrings.
- **Skill 12:** Utilizar o pacote shutil.

## Sobre a Skill 8
Quando a area estiver entre 10.000 e 10.999, o preço estiver entre 5.000.000 e 5.999.999 e tiver mais de 2 quartos execute a linha seguinte
## Recursos Utilizados

- **Python:** Linguagem de programação utilizada para implementar as funcionalidades do tutorial.
- **Pandas:** Biblioteca Python utilizada para manipulação de dados.
- **SMTP Lib:** Biblioteca Python para envio de e-mails via SMTP.

## Exemplo de Desafio

Um exemplo de desafio abordado no tutorial é o seguinte:

"Com base no código pronto de e-mail disponibilizado pelo professor em xx/xx/xxxx, envie um e-mail para cada registro para xxxxxxx@gmail.com com as informações do item anterior."

---

# Biblioteca shutil

A biblioteca `shutil` é uma biblioteca Python usada para operações de alto nível em arquivos e diretórios. Ela fornece funções para copiar, mover, renomear e excluir arquivos e diretórios de uma forma mais fácil e eficiente.

## Principais Recursos

1. **Cópia de arquivos e diretórios**:
   - `shutil.copy(src, dst)`: Copia o arquivo no caminho `src` para o destino `dst`.
   - `shutil.copy2(src, dst)`: Copia o arquivo, preservando as informações de metadados do arquivo original.
   - `shutil.copytree(src, dst)`: Copia um diretório e todo o seu conteúdo para o destino.

2. **Movimento e renomeação de arquivos e diretórios**:
   - `shutil.move(src, dst)`: Move o arquivo ou diretório do caminho `src` para o destino `dst`. Também pode ser usado para renomear arquivos.
   - `shutil.rmtree(path)`: Remove um diretório e todo o seu conteúdo de forma recursiva.

3. **Operações de arquivo**:
   - `shutil.which(cmd)`: Procura pelo executável especificado no caminho do sistema.
   - `shutil.disk_usage(path)`: Retorna uma tupla com o espaço total, usado e livre em bytes no disco do caminho especificado.

4. **Compactação e descompactação de arquivos**:
   - `shutil.make_archive(base_name, format, root_dir=None, base_dir=None)`: Cria um arquivo compactado (zip, tar, etc.) contendo o conteúdo do diretório `root_dir`.
   - `shutil.unpack_archive(filename, extract_dir=None, format=None)`: Descompacta um arquivo compactado.

5. **Operações de arquivo temporário**:
   - `shutil.TemporaryFile()`: Cria um arquivo temporário que é removido automaticamente quando fechado.
   - `shutil.TemporaryDirectory()`: Cria um diretório temporário que é removido automaticamente quando fechado.

A biblioteca `shutil` é extremamente útil para realizar tarefas comuns de manipulação de arquivos e diretórios de forma eficiente e concisa.

Para mais informações, consulte a [documentação oficial](https://docs.python.org/3/library/shutil.html) da biblioteca `shutil`.


**Autor:** [Seu Nome]

**Contato:** [Seu Email]

**Licença:** Este projeto está sob a licença [Licença](link da licença).