# Códigos da Aula 3
# Gabriel Rufino de Souza
# Prof. Abinael Gomes Barreiros - Programação de Computadores

def exercicio1_1():
    # Primeira operação:
    print(10 + 20 * 30)
 
    # Segunda operação:
    print(42 / 30)
 
    # Terceira operação:
    print((94+2) * 6 - 1)
 
 
 
def exercicio1_2():
    a = 10
    b = 20
    c = 30
    total = (a+b)*c
    print(total)
 
 
 
def exercicio1_3():
    y = 42
    x = 30
    w = (y/x)
    print(w)
 
 
 
def exercicio1_4():
    aa = 94
    bb = 2
    cc = 6
    dd = 1
    f = (aa+bb)*(cc+dd)
    print(f)
 
 
 
def exercicio2():
    x = 6
    print(f"Valor antigo: {x}")
    x += 1 # Incrementa o valor da variável 'x' em uma unidade.
    print(f"Valor novo: {x}")
 
 
 
def exercicio3():
    num = float(input("Digite um número com três digitos: "))
    d1 = num // 100
    d2 = num % 100 // 10
    d3 = num % 10
    inverso = d3*100+d2*10+d1
    print("O inverso do número digitado é", inverso)
 
 
 
def exercicio4():
    import math
    num = float(input("Digite um número: "))
    result = math.sqrt(num)
    print(f"O valor da raiz quadrada é {result}")
 


def exercicio4_1():
    import math
 
    num = float(input("Digite um número real: "))
 
    absoluto = math.fabs(num)
    inteiro = math.trunc(num)
    raiz = math.sqrt(absoluto)
    fatorial = math.factorial(inteiro)
 
    print(f"O número absoluto de {num} é:", absoluto)
    print(f"O número Inteiro de {num} é:", inteiro)
    print(f"A raiz de {absoluto} é:", raiz)
    print(f"O fatorial de {inteiro}:", fatorial)
 


def exercicio5_1():
    a = int(input("Digite o valor de A: "))
    b = int(input("Digite o valor de B: "))
    c = int(input("Digite o valor de C: "))
 
    if a > b and c > b:
        print("O menor valor é o de B.")
 


def exercicio5_2():
    a = 33
    b = 33
    if b > a:
        print("'b' é maior que 'a'.")
    elif a == b:
        print("'a' e 'b' são iguais.")
 


def exercicio5_3():
    a = 200
    b = 33
    if b > a:
        print("b é maior que a")
    elif a == b:
        print("'a' e 'b' são iguais")
    else:
        print("'a' é maior que 'b'")
 


def exercicio5_4():
    a = 200
    b = 33
    c = 500
    if a > b and c > a:
        print("Both conditions are True")



