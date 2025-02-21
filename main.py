def calcNota():
    nota1 = int(input("Insira primeira nota: ")) 
    nota2 = int(input("Insira segunda nota: ")) 
    media = (nota1 + nota2) / 2
    print(f"Média final: {media}")

def nome():
    nome = str(input("Digite seu nome: "))
    print("Bom dia", nome)

nome()
