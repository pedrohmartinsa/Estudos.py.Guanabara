
def cadastro():
    pessoa = []
    pessoasCadastradas = []
    while True:
        codigo = int(input('Sua opção: '))
        if codigo > 3 or codigo < 1:
            print('Digite um código válido.')
            continue
        if codigo == 1:
            print(pessoasCadastradas)
            continue
        if codigo == 2:
            nome = str(input('Nome: ')).strip()
            while True:
                try:
                    idade = int(input('Idade: '))
                except (ValueError, TypeError):
                    print('ERRO! Digite um número inteiro válido.')
                    continue
                else:
                    print('Registrado com sucesso.')
                    break
            pessoa.append(nome)
            pessoa.append(idade)
            pessoasCadastradas.append(pessoa[:])
            pessoa.clear()
        if codigo == 3:
            print('Encerrando programa, até logo!')
            break


cadastro()
