# Códigos da Aula 5
# Gabriel Rufino de Souza
# Prof. Abinael Gomes Barreiros - Programação de Computadores

# Exercício 1: O programa pede para o usuário digitar um valor entre 0 e 9, onde caso essa condição seja satisfeita, o programa dirá que o valor está correto, caso contrário, o valor estará incorreto.
def exercicio1():
    num = int(input("Digite um valor entre 0 e 9: "))
    if num >= 0 and num <= 9:
        print("Valor correto")
    else:
        print("Valor incorreto")

# Exercício 2: O programa pede para o usuário dizer qual é o seu turno de trabalho e quantas horas ele trabalha, o programa, baseando-se nessas informações, irá calcular o seu salário.
def exercicio2():
    turno = str(input("Qual é o seu turno de trabalho? (Matutino/Noturno): "))
    print(f"Turno de trabalho: {turno}")
    qntd = int(input("Quantas horas duram o turno?: "))
    print(f"Horas trabalhadas: {qntd}")

    hourSalary = 45.00

    if turno.casefold() == "noturno":
        print(f"Salário: R$ {"{:.2f}".format(qntd * hourSalary)}")
    else:
        print(f"Salário: R$ {"{:.2f}".format(qntd * (hourSalary - 7.5))}")
        