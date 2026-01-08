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
    lista.clear
    tot+=1
print('-='*3,f'SORTEANDO {quant} JOGOS', '-='*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i}: {l}')

