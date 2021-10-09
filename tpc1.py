import random

def menu():
    a = int(input("1-Jogador ou 2-Computador?"))
    escolher(a)

def escolher(a):
    if a == 1:
        inicio = 21
        while inicio > 1:
            valor1 = int(input("Insira um valor: "))
            valor2 = 5 - valor1
            inicio = inicio - 5
            print("O computador tira",valor2)
            print ("Ficam",inicio,"fosforos")
            if inicio == 1:
                print("Perdeu o jogo")
    elif a == 2:
        inicio=21
        while inicio>1:
            valor2=random.randrange(1,4,1)
            print("O computador tira",valor2)
            inicio=inicio-valor2
            print("Ficam",inicio,"fosforos")
            valor1 = int(input('Insira um valor: '))
            inicio = inicio - valor1
            if valor1 + valor2 != 5:
                c = 5 - valor1 - valor2
                print("O computador tira",c)
                inicio = inicio - c
                print("Ficam",inicio,"fosforos")
                while inicio > 1:
                    valor1 = int(input("Insira um valor: "))
                    valor2 = 5 - valor1
                    inicio = inicio -valor1-valor2
                    print("O computador tira",valor2)
                    print("Ficam",inicio,"fosforos")
                    if inicio == 1:
                        print("Perdeu o jogo")
            elif inicio==1:
                print("Ganhou o jogo")
                
menu()
