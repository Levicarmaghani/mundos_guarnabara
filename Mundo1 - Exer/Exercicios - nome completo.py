# Faça um programa que leia o nome completo de uma pessoa
# Mostre o primeiro nome
# Mostre o segundo nome sepaadamente 
nome = str(input("Digite seu nome completo: ")).strip()
lista = nome.split()
ultimo_nome = [len(lista)-1]
print(f'Seu primeiro nome é {lista[0]}\nSeu ultimo nome é {ultimo_nome}: ')