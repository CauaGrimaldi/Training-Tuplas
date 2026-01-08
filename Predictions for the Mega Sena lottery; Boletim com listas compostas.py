from random import randint
lista=list()
jogos=list()
print('-='*50)
print('Jogo da Mega Sena'.center(50))
print('-='*50)
quant=int(input('Quantos jogos você quer que eu sorteie? '))
tot=1
while tot<=quant:
    lista=list()
    cont=0
    while True:
        num=randint(1,60)
        if num not in lista:
            lista.append(num)
            cont+=1
        if cont>=6:
                break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot+=1
print('-='*3,f'SORTEANDO {quant} JOGOS', '-='*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i}: {l}')

ficha=list()
while True:
    nome=str(input('Nome: '))
    nota1=float(input('Nota 1: '))
    nota2=float(input('Nota 2: '))
    m=(nota1+nota2)/2
    ficha.append([nome],[nota1,nota2],[m])
    resp=str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
         break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-='*30)
for i,a in enumerate(ficha):
     print(f'{i:<4}{a[0]:<10}{a[2]:>8.2f}')
while True:
    print('-='*35)
    opc=int(input('Mostrar notas de qual aluno? (999 para parar)'))
    if opc==999:
        break
    if opc<=len(ficha)-1:
         print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
