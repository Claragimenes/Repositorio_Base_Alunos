import time

print("------------------")
print("***** SHEIN *****")
print("------------------")

usuario = input("Digite o nome de usuario: ")
senha = input("Digite a senha: ")

print("Carregando ..........")
time.sleep(3)


if usuario == "admin" and senha == "1234":
    print("Login bem-sucedido!")
    print("------------")
    print(f"Bem vindo ao mercado livre {usuario}")
    print("Usuario ou senha incorretos.")
else:
    print("Usuario ou senha incorretos.")