
def quiz(nome):
    from quiz import main
    print("Bem vindo ao quiz {0}".format(nome))
    main()

def connected4(nome):
    from connected4 import main
    print("Bem vindo ao connected 4 {0}".format(nome))
    main()
def main():
    opt=-1
    fim=False
    nome=input("Qual o seu nome: ")
    while not fim:
        print("1- quiz")
        print("2- Connected 4")
        print("0 Sair")
        opt = int(input("Qual dos jogos quer jogar?: "))

        if opt==1:
            quiz(nome)
        elif opt==2:
            connected4(nome)
        elif opt==0:
            fim=True
        else:
            print("Opt inválida")
