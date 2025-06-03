# Criar uma calculadora usando função
# Criar tambem a opcão de tabuada usando função
# Pergnta a o usuario se ele deseja continuar ou parar(se usuario digita qualque outra letra mostra na tela (INAVALIDO))

# Criando função
def somar (a, b):
    somar = a + b
    return somar
def subtracao (a, b):
    subtrair = a - b 
    return subtrair
def dividir (a, b):
    dividir = a / b
    return dividir
def multiplicar (a, b):
    multiplicar = a * b
    return multiplicar

def tabuada ():
    valor = int(input("Digite um valor para ver sua tabuada: "))
    contador = 0
    for contador in range(0, 11):
        resultado = valor * contador
        print(f"{valor} X {contador} = {resultado} ")
    return resultado
def valores ():
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int (input("Digite o segundo valor: "))
    return valor1, valor2
#Laço de repetição
while True:
    print("-=" * 30)
    print("Bem vindo a calculadora:")
    print("-=" * 30)
    print("Oque voce deseja operar [1]Somar, [2]Subtrair, [3]multiplicar, [4]Dividir, [5]Tabuada do 0 ao 10 ")
    usuario = int(input("Digite uma opção: "))
    while usuario not in [1,2,3,4,5]:
        print("-=" * 30)
        print("OPÇÃO INVALIDA DIGITE NOVAMENTE")
        print("Oque voce deseja operar [1]Somar, [2]Subtrair, [3]multiplicar, [4]Dividir, [5]Tabuada do 0 ao 10 ")
        usuario = int(input("Digite uma opção: "))
    if usuario == 1:
        valor1,valor2 = valores()
        resultado = somar(valor1, valor2)
        print(f"Resultado {valor1} + {valor2} = {resultado}")
    elif usuario == 2:
        valor1,valor2 = valores()
        resultado = subtracao(valor1, valor2)
        print(f"Resultado {valor1} - {valor2} = {resultado}")
    elif usuario == 3:
        valor1,valor2 = valores()
        resultado = multiplicar(valor1, valor2)
        print(f"Resultado {valor1} X {valor2} = {resultado}")
    elif usuario == 4:
        valor1,valor2 = valores()
        resultado = dividir(valor1, valor2)
        print(f"Resultado {valor1} Dividido {valor2} = {resultado:.2f}")
    elif usuario == 5:
        tabuada()
    print("-=" * 30)
    continuar = str(input("Deseja continuar (S/N): ")).strip().upper()
    # Wilhe se usuario digita qualque letra ou palavra difirente o laço se repeti
    while continuar not in "SN":
        print("DIGITO INVALIDO,DIGITA A OPÇÃO VALIDA:")
        continuar = str(input("Deseja continuar (S/N): ")).strip().upper()
    if continuar == "N":
        break
    elif continuar == "S":
        continue
    else:
        print("Essa opção é invalida")
print("-=" * 30)
print("Obrigado volte sempre.")
print("-=" * 30)
        