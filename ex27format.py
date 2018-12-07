def main():
    vezes=int(input("Qual o numero que pretende fazer o quadrado: "))
    for counter in range(0,vezes):
        res=counter**2
        print("{0:<3} squared is {1:<20}".format(counter,res))

    #print("A media dos numeros de 0 a {0} é {1}".format(vezes,(res/vezes)))
