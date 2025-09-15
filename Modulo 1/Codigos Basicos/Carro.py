nome_carro = input("Digite o nome do carro:")
valor_carro = float(input("Digite o valor do carro: R$"))
consumo = input("Digite o consumo por lityro: ")

print("---------------------------")
print(f"| Carro: {nome_carro}")
print(f"| valor: R${valor_carro:.2f}")
print(f"| Consumo: {consumo}km/l")
print("---------------------------")