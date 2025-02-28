def exercicio1():
    n1 = float(input("Qual é a primeira nota?: "))
    n2 = float(input("Qual é a segunda nota?: "))
    print(f"A sua nota é {(n1 + n2) / 2}")

def exercicio2():
    nomes = ["Fernanda", "Miguel", "Leonardo", "Julia", "Célia", "Pablo", "Gabriel", "Dracula", "Daniel", "Otávio" ]
    print(nomes)

def exercicio3():

    amountnames = int(input("Digite a quantidade de nomes: "))

    vetor = []

    for i in range(amountnames):
        names = input(f"Digite o nome da {amountnames - amountnames + 1}° pessoa: ")
        vetor.append(names)

    print(vetor)

def exercicio3():

    nota1 = 5
    nota2 = 9.5
    nome = "Fulano de Tal"
    disci = "Programação de Computadores"
    media = (nota1+nota2)/2

    print(f'Nome do aluno: {nome}\nDisciplina: {disci}\nPrimeira nota: %.2f\nSegunda nota: %.2f' %(nota1,nota2), '\nMedia: {media}')

def exercicio4():
    nome = input("Digite o seu nome: ")
    idade = input("Digite o seu nome: ")
    print("Nome: ", nome, "\nIdade: ", idade)

