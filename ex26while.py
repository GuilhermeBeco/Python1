def main():
    print("Here is a quiz to test your knowledge of farming...")
    print()
    print()
    chances=0
    pontos=0
    print("Question 1")
    while chances!=3:
        print("What percentage of the land is used for farming?")
        print()
        print("a. 25%")
        print("b. 50%")
        print("c. 75%")
        answer = input("Make your choice: ")
        if answer=='c':
            print()
            print()
            print()
            print("Correct")
            print()
            print()
            print()
            pontos=pontos+1
            chances=3
        else:
            print("Wrong")
            print("Try again")
            print()
            print()
            print()
            chances=chances+1
    chances=0
    while chances!=3:
        print("What percentage of the land is used for farming in 2018?")
        print()
        print("a. 30%")
        print("b. 55%")
        print("c. 80%")
        answer=input("Make your choice: ")
        if answer=='b':
            print("Correct!!!!!!")
            print()
            print()
            print()
            pontos=pontos+1
            chances=3
        else:
            print("Wrong")
            print("Try again")
            print()
            print()
            print()
            chances=chances+1
    print("Acertou {0} de 2 perguntas!!".format(pontos))
