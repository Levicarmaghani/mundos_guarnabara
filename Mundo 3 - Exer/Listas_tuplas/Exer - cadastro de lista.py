# Crie um programa onde o usuario posso criar varios valores númericos 
# Cadastrando em uma lista, caso o número já exista la dentro ele não será adicionado
# Pergunte se o usuario deseja continuar, se sim o programa continua perguntado, se não o programa finaliza
# Se o usuario digita um letra errado o programa devera avisar digito invalido 
# No final será exibido todos valores númericos, digitados em ordem crescente
lista = []
while True:
    print("-=" * 20)
    lista_usuario = int(input(f"Digite um valor "))

    if  lista_usuario not in lista: # se o numero da lista do usuario não estiver na minha lista, adiciona
        print("Item adicionado a sua lista ")
        lista.append(lista_usuario) # apeed adicionou o item da lista do usuario para uma lista
    else:
        print("Esse item já existe em sua lista")

    continuar = str(input("Deseja continuar (S/N)")).upper().strip()
    while continuar not in "SN": # Enquanto no meu continuar ou a condição for diferente ou falsa, o laço while vai continuar
    #para sair do while o usuario precisa digita S ou N 
        print(f"DIGITO INVALIDO TENTE NOVAMENTE")
        continuar = str(input("Deseja continuar (S/N)")).upper().strip()
    if continuar == "S":
        continue
    else:
        break
print("-=" * 20)
print(f"Voce digitou os valores {sorted(lista)}")
print("-=" * 20)
