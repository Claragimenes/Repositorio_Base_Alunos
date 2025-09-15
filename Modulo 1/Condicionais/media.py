nome = input("Digite o nome do aluno: ")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota:  "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print("aprovado")
elif media >= 4:
    print("Em recuperação...")
else:
    print("reprovado")

print(f"A madia do aluno {nome} é {media}")
0