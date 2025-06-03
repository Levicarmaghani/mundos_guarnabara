# faça um programa que tenha uma função 
# Chamada contador recebe tres parametros 
# Inicio, Fim, e passo e realize a contagem 
# Seu programa tenque realizar tres contagem atraves da função criada 
# A) De 1 até 10, de 1 em 1
# B) De 10 até 0, de 2 em 2
# C) Uma contagem personalizada 

from time import sleep
# Criando minha função
def contador (inicio, fim, passo):
    # Se o passo for negativo ele vai transformal em positivo 
    if passo < 0:
        passo *= - 1

    # Se o usuario digitar o valor 1 ele é convertido em 1 para evitar um loop infinito 
    if passo == 0:
        passo = 1
    print("-=" * 15)
    print(f"Contagem {inicio} Até {fim} de {passo} em {passo}")
    sleep(0.5)
     # Se o inicio for menor que o fim vamos fazer uma contagem de ordem crescente ex: (0, 20)
    if inicio < fim:
        contador = inicio # Contador pega o valor do inicio 
        # enquanto o valor do contador for meno que o valor do fim 
        while contador <= fim:
            print(f" {contador} " , end='', flush=True)
            sleep(0.5)
            # Contador que esta armazenado o valor do inicio mais o passo que o usuario coloco para puça 
            contador += passo
        print()

    else:
        contador = inicio
        while contador >= fim:
            print(f" {contador}", end='', flush=True)
            sleep(0.5)
            # contador que esta com valor do incicio vai subtrair o valor do usuario 
            contador -= passo
        print()


contador(1 , 10, 1)
contador(10 , 0 , 2)
print("-=" * 15)
print("Agora é sua vez ")
inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(inicio, fim, passo,)
sleep(0.5)

