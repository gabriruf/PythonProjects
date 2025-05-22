# Códigos da Aula de 16/05/25 
# Gabriel Rufino de Souza
# Prof. Abinael Gomes Barreiros - Programação de Computadores



def my_function():
    print("Hello from a function")

my_function() # "Hello from a function"



def soma(a,b):
    result = a + b
    print(result)

soma(4,10) # 14



def exibir_idade(nome, idade=43):
    print(f"{nome} tem {idade} anos.")

exibir_idade("Rafael") # "Rafael tem 43 anos."



def exibir_idade(nome, idade=43):
    print(f"{nome} tem {idade} anos.")

exibir_idade("Rafael", 40) # "Rafael tem 40 anos."



def exibir_idade(nome, idade=43):
    print(f"{nome} tem {idade} anos.")

# palavra-chave como argumento para o parâmetro da função
exibir_idade(nome="Carlos", idade=29) # "Carlos tem 29 anos."



## Função com *args (argumento arbitrários)
def adicao(*args):
    resultado = 0
    for argumento in args:
        resultado = resultado + argumento
    return resultado
#print(adicao(1,2)) # 3
#print(adicao(1,2,4,6)) # 13
#print(adicao(1,2,4,6,8,10)) # 31



# Função com **kwargs (argumentos arbitrários de palavra-chave)
def saudacao(**kwargs):
    if 'nome' in kwargs:
        print(f"Olá, {kwargs['nome']}!")
    else:
        print("Olá, visitante!")

# palavra-chave como argumento para o parâmetro da função
saudacao(nome='Maria') # Olá, Maria!
saudacao() # Olá, visitante!



def apresentar_pessoa(**info):
    print("Informações da Pessoa:")
    for chave, valor in info.items():
        print(f"{chave}: {valor}")

apresentar_pessoa(nome="Mariana", idade=30, profissao="Desenvolvedora")
print("-" * 20)
"""
Informações da Pessoa:
nome: Mariana
idade: 30
profissao: Desenvolvedora
--------------------
"""



def f():
    print("Olá!")

f() # "Olá!"



def f(n):
    print("O valor do parâmetro é", n)

f(10) # "O valor do parâmetro é 10"



def f(n):
    return n

resultado = f(10)
print("O valor do parâmetro é", resultado) # "O valor do parâmetro é 10"



def eleva_quadrado(n):
    return n*n

print(eleva_quadrado(10)) # 100



def eleva_quadrado(n):
    return n**2



def eleva_cubo(n):
    return n**3



def elevado_a_6(n):
    return eleva_quadrado(eleva_cubo(2))

print(elevado_a_6(2)) # 256



def area_triang(base, altura):
    area = (base * altura) / 2
    return area

print(area_triang(4,6)) # 12



area = 0
def area_triang(base,altura):
    area_calc = (base * altura) / 2
    return area_calc
resultado_area = area_triang(4,6)
print(resultado_area)

#area = resultado_area # caso queira atualizar a variável global 'area'
#print(area)



def my_function(food):
    for x in food:
        print(x)
        
fruits = ["apple", "banana", "cherry"]

my_function(fruits) # ['apple', 'banana', 'cherry']



def media(a,b):
    return (a+b)/2

print(media(0,5)) # 2.5
print(media(2,4)) # 3



def converte_para_int(n):
    return int(n)

print(converte_para_int(3.33)) # 3
print(converte_para_int(4.2)) # 4
print(converte_para_int(5.9)) # 5



def celcius_para_fahrenheit(graus_celsius):
    return (graus_celsius * 9 / 5) + 32

print(celcius_para_fahrenheit(25))
print(celcius_para_fahrenheit(0))



## Controle de estoque 
estoque = {}

def adicionar_item(nome, quantidade):
    # Adiciona um novo item ao estoque ou atualiza a quantidade se já existir.
    if nome in estoque:
        estoque[nome] += quantidade
        print(f"Quantidade de '{nome}' atualizada para {estoque[nome]}.")
    else:
        estoque[nome] = quantidade
        print(f"'{nome}' adicionado ao estoque com quantidade {quantidade}.")

def remover_item(nome,quantidade):
    # Remove uma acerta quantidade de um item do estoque.
    if nome in estoque:
        if estoque[nome] >= quantidade:
            estoque[nome] -= quantidade
            print(f"{quantidade} unidades de '{nome}' removidas do estoque. Restam {estoque[nome]}.")
            if estoque[nome] == 0:
                del estoque[nome]
                print(f"'{nome}' acabou no estoque.")
            else:
                print(f"Não há quantidade suficiente de '{nome}' no estoque para remover.j")
        else:
            print(f"'{nome}' não encontrado no estoque.")

def exibir_estoque():
    # Exibe todos os itens e suas respectivas quantidades no estoque
    if estoque:
        print("\n--- Estoque Atual ---")
        for item, quantidade in estoque.items():
            print(f"{item}: {quantidade}")
        print("--------------------------")
    else:
        print("O estoque está vazio.")

# Loop principal para interagir com o usuário
while True:
    print("\n--- Menu ---")
    print("1. Adicionar Item")
    print("2. Remover Items")
    print("3. Exibir estoque")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nome_item = input("Digite o nome do item: ")
        try:
            quantidade_item = int(input("Digite a quantidade e adicionar: "))
            if quantidade_item > 0:
                adicionar_item(nome_item, quantidade_item)
            else:
                print("A quantidade deve ser maior que zero.")
        except ValueError:
            print("Por favor, digite um número inteiro para a quantidade.")
    elif opcao == '2':
        nome_item = input("Digite o nome do item a remover: ")
        try:
            quantidade_remover = int(input("Digite a quantidade a remover: "))
            if quantidade_remover > 0:
                remover_item(nome_item, quantidade_remover)
            else:
                print("A quantidade deve ser maior que zero.")
        except ValueError:
            print("Por favor, digite um número inteiro para a quantidade.")
    elif opcao == '3':
        exibir_estoque()
    elif opcao == '4':
        print("Saindo do controle de estoque.")
        break
    else:
        print("Opção inválida. Por favor, esoclha uma das opções do menu.")
