# Códigos da Aula 5
# Gabriel Rufino de Souza
# Prof. Abinael Gomes Barreiros - Programação de Computadores

# Exercício 1: Lê a entrada da variável 'idade', feita pelo usuário, e imprime na tela a classificação correspondente ao valor da variável.
def exercicio1():
    idade = int(input("Digite a sua idade, seu fella: "))
    
    if idade <= 11:
        print("Criança.")
    elif idade > 11 and idade <= 18:
        print("Adolescente.")
    elif idade > 18 and idade <= 24:
        print("Jovem.")
    elif idade > 24 and idade <= 40:
        print("Adulto.")
    elif idade > 40 and idade <= 60:
        print("Meia Idade.")
    else:
        print("Idoso.")

# Exercício 2: Lê a entrada feita pelo usuário de dois valores, e analisa para saber qual variável é maior, imprimindo na tela qual variável é a maior.
def exercicio2():
    primeiro_valor = int(input("Digite o primeiro valor: "))
    segundo_valor = int(input("Digite o segundo valor: "))
    print("Primeiro" if primeiro_valor > segundo_valor else "Segundo")
    #if primeiro_valor > segundo_valor:
    #    print("Primeiro")
    #else:
    #    print("Segundo")

# Exercício 3: O programa contém uma variável com uma lista com varios números, o usuário é requisitado para digitar um número, onde caso esse número exista ou não na lista, o programa imprime na tela dizendo se existe ou não existe.
def exercicio3():
    numeros = [1,3,6,10,5,23]
    numero_digitado = int(input("Digite um número: "))
    if numero_digitado in numeros:
        print(f"O número {numero_digitado} está na lista.")
    else:
        print(f"O número {numero_digitado} não está na lista.")
    