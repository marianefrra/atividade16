# Crie um programa que receba o peso e a altura de uma pessoa e calcule o Índice de Massa Corporal (IMC). O programa deve classificar o IMC da pessoa de acordo com a tabela a seguir:
# Abaixo do peso: IMC < 18.5
# Peso normal: 18.5 ≤ IMC < 25
# Sobrepeso: 25 ≤ IMC < 30
# Obesidade: IMC ≥ 30


peso = float(input("digite seu peso em KG"))
altura = float(input("digite sua altura M"))


 #cauular o IMC

IMC = (peso/altura**2)
print(IMC)

#classificação

if IMC <18.5:
    print("você esta abaixo do peso")
elif 18.5 <= IMC <25:
    print("você está acima do peso")
elif 25 <= IMC <30:
    print("você está sobrepeso")
elif IMC >= 30:
    print("você está com obesidade")