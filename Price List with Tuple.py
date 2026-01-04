listagem=('Lápis', 1.75,
          'Borracha', 2.00,
          'transferidor',3.00,
          'Caderno',7.00,
          'Caneta', 9.00,
          'Livro', 6.00,
          'Régua',10.00)
print('-'*40)
print(f'{'LISTAGEM DE PREÇOS':^40}')
print('-'*40)
for pos in range(0,len(listagem)):
    if pos%2==0:
        print(f'{listagem[pos]:.<30}', end='')   
    else:
        print(f'R${listagem[pos]:>5.2f}') 
print('-'*40)