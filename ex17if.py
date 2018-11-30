def main():
    num=int(input("Indique um numero: "))
    if num>20:
        print("Numero a cima do limite")
    elif num<1:
        print("Numero abaixo do limite")
    else:
        print("O seu numero está entre o limite de 1 e 20")
