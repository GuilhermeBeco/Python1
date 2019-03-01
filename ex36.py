def main():
    animals = []
    for counter in range(0,6):
        animals.append(input("Insira um animal "))

    opt=int(input("Quer apresentar a lista na ordem em que inseriu(1) ou na reversa(2): "))
    if opt==1:
        print(animals[0:len(animals)])
    if opt==2:
        animals.reverse()
        print(animals[0:len(animals)])
    if opt!=2 and opt!=1:
        print("opt inválida")
