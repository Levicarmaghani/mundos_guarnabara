# Desenvolva uma logica que desenvolve o peso e a altura de uma pessoa 
# Calcule se imc, e mostre seu status, de acordo com a tabela abaixo 
# Abaixo de 18.5: abixo do peso
# Entre 18.5 e 25: peso ideal 
# 25 até 30: Sobre peso 
# 30 até 40: obesidade  
#acima de 40: obesidade morbida 

altura = float(input("\033[1;34;40mQual é sua altura?\033[m "))
peso =  float(input("\033[1;30;40mQuanto é seu peso?\033[m "))
imc =  peso / ( altura * altura)

if imc < 18.5:
    print(f'\033[1;36;40mimc = {imc:.2f} abaixo do peso\033[m')

elif imc < 25:
    print(f"\033[1;36;40mimc = {imc:.2f} peso ideal\033[m")
elif imc < 30:
    print(f"\033[1;31;40mimc = {imc:.2f} sobre peso\033[m ")

elif imc < 40:
    print(f"\033[1;31;40mimc = {imc:.2f} obesidade\033[m ")

else:
    print(f"\033[1;31;40mimc = {imc:.2f} obesidade morbita\033[m ")
          