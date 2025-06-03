from random import shuffle
aluno1 = str(input("Aluno1: ")) 
aluno2 = str(input("Aluno2: "))
aluno3 = str(input("Aluno3: "))
aluno4 = str(input("Aluno4: "))

lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)

print(f"Ordem de entrega dos trabalhos {lista}")