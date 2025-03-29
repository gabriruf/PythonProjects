# Códigos da Aula 6
# Gabriel Rufino de Souza
# Prof. Abinael Gomes Barreiros - Programação de Computadores

# O programa contém uma variável pre-definida, cuja qual é avaliada em um laço de condição para ver se o resultado condiz com as opções descritas, caso não seja, o programa responde dizendo que não é nenhuma das três opções.
def exercicio1():
    ling = "C++"
    if ling == "C++":
        print("C++ é uma linguagem de programação compilada")
    elif ling == "Python":
        print("Python é uma lingaugem de programação de alto nível")
    elif ling == "Java":
        print("Java é uma linguagem de programaçã amplamente utilizada no mercado")
    else:
        print("Não é nenhuma das três opções.")



# O programa pede para o usuário escrever a sua média e o percentual de frequência, o programa então avalia as seguintes condições: caso o percentual for menor que 75%, o aluno é reprovado por falta, caso o percentual seja maior ou igual a 75%, mas sua média seja menor que 6, o aluno é reprovado por nota, se nenhuma das condições anteriormente descritas forem corretas, o aluno é aprovado.
def exercicio2():
    media = float(input("Digite a média do aluno: "))
    percent = float(input("Digite o percentual de frequência: "))

    if (percent < 75):
        print("Reprovado por falta.")
    elif (percent >= 75 and media < 6):
        print("Reprovado por nota")
    else:
        print("Aprovado")



# O programa pede o tipo e o número de diárias que o usuário irá contratar, se baseando nesses resultados, o programa mostrara o tipo de diaria escolhida e o valor a pagar considerando o valor base e a quantidade de dias. Caso o usuário insira um valor incorreto, o programa dirá que o tipo de diária é inválido.
def exercicio3():
    diariaType = str(input("Digite o tipo da diária: "))
    numDiarias = int(input("Digite o número de diárias: "))
    if diariaType.casefold() == "s":
        num = 255.90
        print("Tipo de diária: Quarto Simples:")
        print(f"Valor a pagar: R$ {(num * numDiarias):.2f}")
    elif diariaType.casefold() == "d":
        num = 305.50
        print("Tipo de diária: Quarto Duplo:")
        print(f"Valor a pagar: R$ {(num * numDiarias):.2f}")
    elif diariaType.casefold() == "t":
        num = 360.50
        print("Tipo de diária: Quarto Triplo:")
        print(f"Valor a pagar: R$ {(num * numDiarias):.2f}")
    else:
        print("tipo de diária inválido.")



# Esse programa pede que o usuário digite três números, logo após isso, o programa checa com um "if" para saber qual das variáveis possui o número maior.
def exercicio4():
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    n3 = int(input("Digite o terceiro número: "))

    if n1 > n2 and n1 > n3:
        print("O primeiro número é o maior")
    elif n2 > n1 and n2 > n3:
        print("O segundo número é o maior")
    else:
        print("O terceiro número é o maior")



# Esse programa pede para o usuário o valor da compra, e o desconto para essa compra. Logo após isso, o programa calcula o desconto com o valor da compra, mostrando o valor com desconto que o usuário irá pagar.
def exercicio5():
    valor_orig = float(input("Digite o valor da compra: R$ "))
    desconto = float(input("Desconto (em %) para essa compra: "))
    desconto = desconto / 100
    print(f"Valor original: R$ {valor_orig}")
    print(f"Desconto ganho: R$ {valor_orig * desconto}")
    print(f"Valor com desconto: R$ {valor_orig * (1-desconto)}")



# O programa pede os quatro digitos da placa do carro do usuário, com esse valor, ele vai pegar o último digito da placa, usando o operador de módulo, logo após isso, será checado esse número para ver em qual dia o carro não pode circular.
def exercicio6():
    placa = int(input("Digite os quatro digitos da placa"))
    final = placa % 10
    if final == 1 or final == 2:
        print("O veículo não pode circular as segundas-feiras")
    elif final == 3 or final == 4:
        print("O veículo não pode circular as terças-feiras")
    elif final == 5 or final == 6:
        print("O veículo não pode circular as quartas-feiras")
    elif final == 7 or final == 8:
        print("O veículo não pode circular as quintas-feiras")
    else:
        print("O veículo não pode circular as sextas-feiras")