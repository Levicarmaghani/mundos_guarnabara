# Desenvolva um programa que leia o comprimento de tres retas
# diga ao usuario se elas podem o não formar um triangulo
print("-="*20)
print("Analisador de triangulo")
print("-="*20)
r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("terceiro segmento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f"Os segmentos acima podem forma triangulo:")
    if r1 == r2 == r3:
        print('Triangulo "EQUILATERO"')
    elif r1 != r2 != r3 != r1:
        print('Triangulo "ESCALENO"')
    else:
        print('ISÓSCELES')
else:
    print(f"Os segmentos acima não podem formar um triangulo: ")


