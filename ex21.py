def main():
    switch1=int(input("Qual o estado do primeiro switch: "))
    switch2=int(input("Qual o estado do segundo switch: "))

    if switch1==1 and switch2==1:
        print("A luz está ligada")
    else:
        print("A luz está desligada")
