def main():
    quiz=[]
    fim=False
    opt=10
    #pergutnas
    i=0
    certa=0
    perg=""
    r=[]
    #respostas
    p=[]
    sc=0
    resposta=-1


    while fim==False:
        print("QUIZ!!!!")
        print("Escolha a opt pretendida")
        print("1-Criar pergunta")
        print("2-Responder quiz")
        print("0-Sair")
        opt=int(input("Qual a sua opt: "))
        if opt==1:
            perg=input("Insira a sua pergunta: ")
            while i<=3:
                r.append(input("Insira uma resposta: "))
                i+=1
            certa=int(input("Qual das 4 respostas é a verdadeira: "))
            quiz.append([perg,r,certa])

            certa=0
            i=0
            perg=""
            r=[]
        if opt==2:
            for pergunta in quiz:
                print(pergunta[0])
                p=pergunta[1]
                print(p[0:4])
                resposta=pergunta[2]
                if int(input("Qual a resposta: "))==resposta:
                    print("Congrats")
                    sc+=1
                else:
                    print("Better luck next m8")
            print("A sua pontuação foi de {0}/{1} respostas certas".format(sc,len(quiz)))
            sc=0
        if opt==0:
            fim=True
