temp=[]
princ=[]
mai=men=0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ)==0:
        mai=men=temp[1]
    else:
        if temp[1]>mai:
            mai=temp[1]
        if temp[1]<men:
            men=temp[1]
    princ.append(temp[:])
    temp.clear()
    resp=(str(input('Quer continuar? [S/N]')))
    if resp in 'Nn':
        break
print('-='*30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mai}kg. Peso de ',end='')
for p in princ:
    if p[1]==mai:
        print(f'{p[0]}', end='')
print()
print(f'O menor peso foi de {men}kg. Peso de ', end='')
for p in princ:
    if p[1]==men:
        print(f'{p[0]} ', end='')
print()

núm=[[],[]]
valor=0
for c in range(1,8):
    valor=int(input(f'Digite o {c}º valor: '))
    if valor%2==0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
print('-='*30)
print(f'Os valores pares digitados foram: {núm[0]}. ')
print(f'Os valores ímpares digitados foram: {núm[1]}.')

matriz=[[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()