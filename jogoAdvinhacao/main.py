import random

def jogoAdvinhacao():
    secretNum = random.randint(1,50)

    for i in range(10):
        palpite = int(input("Advinhe um número: "))

        if palpite == secretNum:
            print("Parábens! Você acertou o número")
            break
        elif palpite > secretNum:
            print("Tente um número menor.")
        else:
            print("Tente um número maior.")

    print("Fim do jogo. O número secreto era:", secretNum)

jogoAdvinhacao()