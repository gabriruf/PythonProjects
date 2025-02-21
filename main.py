def calcNota():
    nota1 = int(input("Insira primeira nota: ")) 
    nota2 = int(input("Insira segunda nota: ")) 
    media = (nota1 + nota2) / 2
    print(f"Média final: {media}")

def nome():
    nome = input("Digite seu nome: ")
    curso = input("Digite o curso: ")
    disci = input("Digite a disciplina: ")

    produtos = ["Computador", "Mouse", "Teclado", "Pendrive", "Monitor", "Celular", "HD", "Modem", "Roteador", "Webcam"]

    print(f"{produtos}")

    print(f"Bom dia {nome}")
    print(f"Curso: {curso}")
    print(f"Disciplina: {disci}\n")
    print(f"{produto}")

nome()
