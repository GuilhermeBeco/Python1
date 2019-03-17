import csv
import random
def ranQuestions(quiz,num):
    i=0
    p=[]
    while i<num:
        j=random.randint(0,len(quiz))
        p.append(quiz[j])
        #falta verificacao de repeat
        i+=1
    return p

def get_questions():
    questions = []
    with open("farming.csv", mode="r", encoding="utf-8") as my_file:
        reader = csv.reader(my_file)
        for row in reader:
            questions.append(row)
    return questions

def main():
    quiz=[]
    fim=False
    opt=10
    #respostas
    p=[]
    quiz=get_questions()
    questions=[]
    sc=0


    while fim==False:

        print("QUIZ!!!!")
        print("Escolha a opt pretendida")
        print("1-Responder quiz")
        print("0-Sair")
        opt=int(input("Qual a sua opt: "))
        if opt==1:
            num=int(input("Quantas perguntas quer responder: "))
            questions=ranQuestions(quiz,num)
            for q in questions:
                for printQuestions in range(0,len(q)-1):
                    print(q[printQuestions])
                resposta=input("Qual a sua resposta: ")
                if resposta==q[len(q)-1]:
                    print("congrats")
                    sc+=1
                else:
                    print("Better luck next time m8")
        print("A sua pontuação foi de {0}/{1} respostas certas".format(sc,num))
           # sc=0
        if opt==0:
            fim=True
