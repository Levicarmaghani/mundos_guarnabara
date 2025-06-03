# Solicite uma frase para o usuario e conte quantas vogais tem a frase.

# Entradas, Frase solicitada
quantidades_de_vogais = 0 
frase = input("Informe uma frase: ")

for letra in frase.lower():
    # if letra.lower() in {"a", "e", "i", "o", "u",}:
    if letra in "aeiou":
        # quantidades de vogais = quantidades_vogais + 1
        quantidades_de_vogais += 1

        print(f'A frase "{frase}" tem {quantidades_de_vogais} vogais')

     
              