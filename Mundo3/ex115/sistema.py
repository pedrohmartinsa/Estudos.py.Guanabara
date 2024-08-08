from lib.interface import *
from lib.arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    escolha = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if escolha == 1:
        # mostrar o arquivo com as pessoas
        leiaArquivo(arq)
    elif escolha == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = readInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif escolha == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        erro('ERRO! Escolha uma opção válida')
    sleep(1)

