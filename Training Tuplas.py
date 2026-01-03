cont = ('zero', 'one', 'two', 'three', 'four',
        'five', 'six', 'seven', 'eight', 'nine',
        'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
        'fifteen', 'sixteen', 'seventeen', 'eighteen',
        'nineteen', 'twenty')
while True:
    while True:
        n=int(input('Type a number between 0 to 20:'))
        if 0 <= n <=20:
            break
        print('Try again.', end='')
    print(f'You typed the number {cont[n]}')
    resp=input('Do you want to continue? [Y/N]').strip().upper()
    if resp !='Y':
        break
print('Program finished.')

teams=('Flamengo', 'Palmeiras', 'Cruzeiro', 'Mirassol',
       'Fluminense', 'Botafogo', 'Bahia', 'São Paulo',
        'Grêmio', 'Red Bull Bragantino', 'Atlético-MG',
        'Santos', 'Corinthians', 'Vasco da Gama',
        'Vitória', 'Internacional', 'Ceará', 'Fortaleza', 'Juventude', 'Sport')
print('-='*15)
print(f'List of teams:{teams}')
print('=-'*15)
print(f'The first 5 teams are:{teams[0:5]}')
print('=-'*15)
print(f'The last 4 teams are:{teams[-4:]}')
print('-='*15)
print(f'Teams in alphabetic order:{sorted(teams)}')
print('-='*15)
print(f'The Ceará are in {teams.index('Ceará')+1}ª position.')

from random import randint
n=(randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print('The numbers raffled were: ', end='')
for c in n:
    print(f'{n}', end='')
print(f'The highest number raffled was:{max(n)}.')
print(f'The lowest value raffled was: {min(n)}.')

n=(int(input('Type a number: ')),
    int(input('Type another number: ')),
        int(input('Type one more number: ')),
        int(input('Type the last number: ')))
print(f'You typed the values: {n}')
print(f'The value 9 appeared {n.count(9)} times.')
if 3 in n:
    print(f'The number 3 appeared in the position {n.index(3)+1}º ')
else:
    print('The value 3 was not entered in any position.')
print('The even values ​​entered were:', end='')
for c in n:
    if n%2==0:
        print(n, end=' ')