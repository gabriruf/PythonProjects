# Códigos da Aula 4
# Gabriel Rufino de Souza
# Prof. Abinael Gomes Barreiros - Programação de Computadores

# Exemplos de aplicação
# Exemplo 1: Programa que solicita a idade do usuário e mostra se ele pode ter CNH
def exemplo1():
    idade = int(input("Digite a sua idade: "))
    
    if idade >= 18:
        print("Parabéns! Você pode ter CNH.")
    else:
        print("Você não pode ter CNH.")



# Exemplo 2: Programa que solicita um número inteiro a usuário e mostre-o caso o mesmo seja par.
def exemplo2():
    num = int(input("Insira um número inteiro: "))
    if num % 2 == 0:
        print(f"O número: {num} é par.")
    else:
        print(f"O número: {num} é impar.")



# Exemplo 3: Programa que executa o valor da variável enquanto a condição do loop 'while' não é satisfeita.
def exemplo3():
    i = 1
    while i <= 6:
        print(i)
        i += 1



# Exemplo 4: Similar ao anterior, exceto que quando a condição do loop é aceita e ela deixa de ser verdade, um print é executado no bloco else dizendo que todos os números foram executados.
def exemplo4():
    i = 1
    while i < 6:
        print(i)
        i += 1
    else:
        print("Parabéns, exibiu todos os números.")



# Exemplo 5: Programa que contém uma variável que armazena uma tupla com strings, que é armazenada dentro de uma variável "x" por meio de um loop "for", e depois o valor é impresso na tela.
def exemplo5():
    fruits = ("maçã", "banana", "cereja")
    for x in fruits:
        print(x)



# Exemplo 5_1: Similar ao anterior, porém agora é possível indexar um item específico da tupla dentro do loop "for", de forma que o resultado só mostra a string indexada anteriormente. Foi necessário alterar o caractér que o print usa quando sua execução termina, que é um \n, usada para fazer com que o texto seguinte
def exemplo5_1():
    fruits = ("maçã\n", "banana\n", "cereja\n")
    for x in fruits[1]:
        print(x, end = "")



# Exemplo 6: Este código recebe a entrada do usuário para duas notas, que são calculadas em uma média aritmética, onde se o resultado for maior ou igual a 6, a pessoa é aprovada, caso contrário a pessoa é reprovada.
def exemplo6():
    a1 = int(input("Digite a nota da A1: "))
    a2 = int(input("Digite a nota da A2: "))

    media = (a1+a2)/2
    if media >= 6.0:
        print("Aprovado!!!")
    else:
        print("Reprovado!!!")



# Exemplo 7: Este código recebe a entrada de um usuário para um número inteiro, onde se ele for maior do que 0, vai ser calculada a raiz quadrada desse número, com arredondamento para 2 casas decimais, se o número for menor que zero, o programa não irá calcular pois o número é negativo.
def exemplo7():
    import math

    num = int(input("Digite um número qualquer: "))
    if num > 0:
        raiz = math.sqrt(num)
        print(f"A raiz quadrada do número digitado é: {raiz:.2f}")
    else:
        print("Não é possível calcular raiz quadrada de número negativo")



