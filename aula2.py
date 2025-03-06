# Feito por Gabriel Rufino
# Prof. Abinael Gomes - Programação de Computadores
def exercicio1():
    n1 = float(input("Qual é a primeira nota?: "))
    n2 = float(input("Qual é a segunda nota?: "))
    print(f"A sua nota é {(n1 + n2) / 2}")

def exercicio2():
    a = int(input("Digite o 1° valor: "))
    b = int(input("Digite o 2° valor: "))
    print(f"A soma é {a+b}\nA subtração é {a-b}\nA multiplicação é {a*b}\nA divisão é {a/b}\nO resto da divisão é {a%b}")

def exercicio3():
    a = float(input("Digite o 1° valor: "))
    b = float(input("Digite o 2° valor: "))
    media = (a+b)/2
    print(f"A média é {media}")

def exercicio4():
    nomes = ["Fernanda", "Miguel", "Leonardo", "Julia", "Célia", "Pablo", "Gabriel", "Dracula", "Daniel", "Otávio" ]
    print(nomes)

def exercicio5():
    amountnames = int(input("Digite a quantidade de nomes: "))

    vetor = []

    for i in range(amountnames):
        names = input(f"Digite o nome da {amountnames - amountnames + 1}° pessoa: ")
        vetor.append(names)

    print(vetor)

def exercicio6():
    nota1 = 5
    nota2 = 9.5
    nome = "Fulano de Tal"
    disci = "Programação de Computadores"
    media = (nota1+nota2)/2

    print(f'Nome do aluno: {nome}\nDisciplina: {disci}\nPrimeira nota: %.2f\nSegunda nota: %.2f' %(nota1,nota2), f'\nMedia: {media}')

def exercicio7():
    nome = input("Digite o seu nome: ")
    idade = input("Digite o seu nome: ")
    print("Nome: ", nome, "\nIdade: ", idade)

def exercicio8_1():
    a = int(input("Digite o valor de A: "))
    b = int(input("Digite o valor de B: "))
    c = int(input("Digite o valor de C: "))

    if a > b and c > b:
        print("O menor valor é o de B.")

def exercicio8_2():
    a = 33
    b = 33
    if b > a:
        print("'b' é maior que 'a'.")
    elif x == y:
        print("'a' e 'b' são iguais.")

def exercicio8_3():
    a = 200
    b = 33
    if b > a:
        print("b é maior que a")
    elif a == b:
        print("'a' e 'b' são iguais")
    else:
        print("'a' é maior que 'b'")
