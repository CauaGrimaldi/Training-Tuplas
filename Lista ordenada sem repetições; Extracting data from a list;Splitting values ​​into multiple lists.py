lista=[]
for c in range(0,5):
    n=int(input('Digite um valor:'))
    if c==0 or n>lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos=0
        while pos<len(lista):
            if n<=lista[pos]:
                lista.insert(pos,n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos+=1
print('-='*30)
print(f'Os valores digitados em ordem foram: {lista} ')

valores=[]
while True:
    valores.append(int(input('Digite um valor:')))
    resp=str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-='*30)
print(f'Você digitou {len(valores)} elementos. ')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}.')
if 5 in valores:
    print('O número 5 faz parte da lista!')
else:
    print('O Valor 5 não foi encontrado na lista.')

num=list()
pares=list()
ímpares=list()
while True:
    num.append(int(input('Digite um número: ')))
    resp=str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v%2==0:
        pares.append(v)
    elif v%2==1:
        ímpares.append(v)
print('-='*30)
print(f'A lista completa é {num} ')
print(f'A lista de pares é {pares} ')
print(f'A lista de ímpares é {ímpares} ')

expr=str(input('Digite a expressão: '))
pilha=[]
for símb in expr:
    if símb=='(':
        pilha.append('()')
    elif símb==')':
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha)==0:
    print('Sua expressão está válida.')
else:
    print('Sua expressão está errada.')