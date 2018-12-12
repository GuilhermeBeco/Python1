import math
def main():
    numero=int(input("Qual o numero que pretende converter para binário:"))
    ##res=bin(numero)
    s = ''
    while numero:
        if numero & 1 == 1:
            s = "1" + s
        else:
            s = "0" + s
        numero //= 2
        print(numero)
    print(s)
