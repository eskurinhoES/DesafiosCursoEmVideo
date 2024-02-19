"""Script que lê a data de nascimento de uma pessoa e mostra a data
formatada."""

nome = input('Qual o seu nome? ')
dia = int(input('Qual o dia do seu nascimento? '))
mes = input('Qual o mês de seu nascimento? ')
ano = int(input('Qual o ano de seu nascimento? '))
print(f'Olá {nome}!')
print(f'Você nasceu no {dia} de {mes} de {ano}. Correto? ')
