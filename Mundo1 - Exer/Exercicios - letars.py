# Crie um programa que leia o nome completo de uma pessoa
# O nome com todas letras maisculas
# O nome com todas letras minusculas
# Quantas letra ao todo sem considerar o espaço
# Quantas letras tem o primeiro nome
nome = input("Dgita seu nome completo: ")
maiuscula = nome.upper()
minuscula = nome.lower()
removedor_espaço = nome.replace(" ","")
quantidade_letras = len(removedor_espaço)
lista = nome.split()
letras_primeiro_nome = len(lista[0])
print(f"{maiuscula}\n{minuscula}\n{quantidade_letras}\n{lista}\n{letras_primeiro_nome}")