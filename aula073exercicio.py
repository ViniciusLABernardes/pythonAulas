nome = input("digite o nome: ")
idade = input("digite sua idade: ")
idade = int(idade)
salario = input("digite seu salario: ")
salario = float(salario)
sexo = input("coloque f se mulher m se homem")
sexo_opcoes = ["f","m"]
estado_civil = ["s","c","v","d"]

if len(nome) < 3:
    print("nome invalido")
else:
    print(nome)


if idade < 0:
    print("idade invalida")
elif idade > 150:
    print("vei demais")
else:
    print(idade)


if salario <= 0:
    print("salario invalido")
else:
    print(salario)


if sexo == sexo_opcoes[0]:
    print("mulher")
else:
    print("homem")