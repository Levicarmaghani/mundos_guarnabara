# Crie um programa que leia o nome completo de uma pessoa
# O nome com todas letras maisculas
# O nome com todas letras minusculas
# Quantas letra ao todo sem considerar o espaço
# Quantas letras tem o primeiro nome

nome = str(input("Digita seu nome ineteiro: "))
maiscula = nome.upper()
minuscula = nome.lower()
sem_espaço = nome.replace(" ", "")
Soma_letra = len(sem_espaço)
primeira_palavra = nome.split()
quantdeletras = len(primeira_palavra[0])
print(f'{maiscula}\n{minuscula}\n{Soma_letra}\n{quantdeletras}')

