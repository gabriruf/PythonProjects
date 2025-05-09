# Desafio 6 - Advinhe meu número: Crie um jogo onde o computador escolhe um número inteiro aleatório entre 0 a 100.
def desafioAdvinhacao():
    from random import randint 
    import os
    import sys

    num = randint(0,100)

    tentativa = 0

    for tentativa in range(5):
        numInput = int(input("Digite um número entre 0 e 100.\n> "))

        if (numInput < num):
            print("Tente um número maior.")
        elif (numInput > num):
            print("Tente um número menor.")
        else:
            os.system('cls' if os.name == "nt" else 'clear')
            print("Parabéns, você acertou.")
            print(f"O número secreto é: {num}")
            sys.exit()

    os.system('cls' if os.name == "nt" else 'clear')
    print(f"Fim de jogo!!!\nO número secreto era {num}")
    


# Exercício 1: Escreva um programa em Python que use um loop for para imprimir uma contagme regressiva de 10 a 1.
def exercicio1():
    for i in range(10,0,-1):
        print(i)



# Exercício 2: Escreva um programa que use um loop while para calcular a soma de todos os números pares de 1 a 100.
def exercicio2():
    soma = 0
    numero = 2
    while numero <= 100:
        soma += numero
        numero += 2

    print("A soma dos números pares de 1 a 100 é: ", soma)



# Exercício 3: Escreva um programa que peça ao usuário um número inteiro e imprima a tabuada desse número de 1 a 10 usando um loop for.
def exercicio3():
    numero = int(input("Digite um número inteiro: "))
    for i in range(1,11):
        print(numero, "x", i, "=", numero * i)



# Exercício 4: Escreva um programa que peça ao usuário um número inteiro e calcule o fatorial desse número usando um loop while.
def exercicio4():
    numero = int(input("Digite um número inteiro: "))
    fatorial = 1
    i = 1

    while i<=numero:
        fatorial *= i
        i += 1
    
    print(f"O fatorial de {numero} é: {fatorial}")



# Exercício 5: Escreva um programa que imprima todos os números primos de 1 a 100 usando um loop for e uma estrutura condicional if dentro do loop.
def exercicio5():
    for numero in range(2,101):
        primo = True
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                primo = False
                break
            if primo:
                print(numero)