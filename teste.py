from time import sleep

'''nome = input('Olá, como posso te chamar?')
print(f'Seja bem vindo a calculadora, {nome}')
n1 = int(input('Escolha um número:'))
n2 = int(input('Escolha outro número:'))
s = n1 + n2
print(f'a soma de {n1} e {n2} é igual a {s}')'''

#listas
'''lista = [1, 10, 100, 1000]
print(lista[0]) # primeiro elemento = 1.
print(lista[-1]) # ultimo elemento = 1000.'''

#If, Else
'''tempo = int(input('Digite o tempo de uso do seu carro: '))
if tempo <= 3:
    print('carro novo')
else:
    print('carro velho')
print('--FIM--')'''

#adicionar cor
#\033[0;30;41m
'''print('\033[0;30;41mvamo\033[m')'''

#ordenando lista
'''a1 = input('Primeiro número:')
a2 = input('Segundo número:')
a3 = input('Terceiro número:')
a4 = input('Quarto número:')
lista = [a1, a2, a3, a4]
lista.sort()
print(f'O menor número é {lista[0]} e o maior é {lista[-1]}')'''

#laço
'''from time import sleep
n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
    sleep(0.5)
print('FIM')'''

#Início da contagem, fim da contagem, e quantos números é pra pular de um para o outro
'''from time import sleep
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
    sleep(0.5)'''

#mostra a frase ao contrário
'''frase = input('Digite uma frase: ')
print(frase[::-1])'''

#contagem com while
'''from time import sleep 
c = 0
while c < 10:
    c += 1
    print(c)
    sleep(0.5)
print('acabou')'''

#contador usando True e break
'''from time import sleep
cont = 0
while True:
    cont += 1
    print(cont)
    sleep(1)
    if cont == 10:
        print('FIM.')
        break'''

#sem contar o 999 sem usar gambiarra
'''n = s = 0
while True:
    n = int(input('Digite um número:'))
    if n == 999:
        break #para parar o código 
    s += n #posicionado aqui para não contar o 999
print(f'A soma entre eles é igual a {s}')'''


#diferentes formas de manipular a tupla usando for
'''lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')'''

'''for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')'''

'''for cont in range(0, len(lanche)):
    print(f' vou comer {lanche[cont]} na posição {cont}')'''


'''for comida in lanche:
    print(f'Eu vou comer {comida}.')
print('To cheio.')'''

#para ordenar a tupla
'''lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')

print(sorted(lanche))'''


'''galera = []
dados = []

while True:
    dados.append(str(input('Nome:')))
    dados.append(int(input('Peso:')))
    galera.append(dados[:])
    dados.clear()

    r = str(input('Deseja continuar?[S/N] '))
    while r not in 'SsNn':
        r = str(input('Deseja continuar?[S/N] '))
    if r in 'Nn':
        break

for p in galera:
    print(p[1])'''

#dicionario estruturas
'''
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
pessoas['peso'] = 78.6 #adiciona um item
for k in pessoas.keys():
    print(k)
print()
for v in pessoas.values():
    print(v)
print()
for k,v in pessoas.items():
    print(f'{k} = {v}')
'''
def n(*num):
    print(num)


n(12, 15, 20)
