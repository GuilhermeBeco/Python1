def main():
    vezes=int(input("Quantos numeros pretende fazer a média: "))
    res=0
    for counter in range(0,vezes):
        res+=counter
        print(res)

    print("A media dos numeros de 0 a {0} é {1}".format(vezes,(res/vezes)))
