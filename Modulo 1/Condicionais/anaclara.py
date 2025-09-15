nome = input("Digite seu nome: ")
peso = float(input("Digite o peso da pessoa: "))
altura = float(input("Digite a aultura da pessoa: "))

imc = peso / (altura * altura)

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 24.9:
    print("peso normal")
elif imc < 29.9:
    print("sobrepeso")
elif imc < 34.9:
    print("Obesidade grau I")
elif imc < 39.9:
    print("Obesidade grau II")
else:
    print("Obesidade grau III")


print(f"O nome do paciente é: {nome}\nE o IMC é: {imc}")
