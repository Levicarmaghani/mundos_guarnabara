# A confederação de natação precisa de um programa que leia o ano de nascimento de um atleta
# Mostre sua categoria de acordo com a idade 
# Até 9 anos mirim: Até 14 anos infantil: Até 19 anos: Junior Até 20 anos: senior Acima master 

from datetime import date
atual = date.today().year
nascimento = int(input('Qual ano voce nasceu? '))
idade = atual - nascimento

if idade <= 9:
    print(f"Sua idade: {idade} categoria Mirim. ")
elif idade <= 14:
    print(f"Sua idade: {idade} categoria infantil. ") 
elif idade <= 19:
    print(f"Sua idade: {idade} categoria junior.  ")

elif idade <= 25:
     print(f"Sua idade {idade} categoria senior. ")
else:
    print(f"Sua idade {idade} categoria master. ")