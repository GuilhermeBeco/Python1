import math
def main():
    valDolar=float(input("Insert the amount to convert: "))
    rate=0.88
    valEuro=int(valDolar*rate)
    notas50=valEuro//50
    res50=valEuro-notas50*50

    notas20=res50//20
    res20=res50-notas20*20

    notas10=res20//10
    res10=res20-notas10*10

    notas5=res10//5
    res5=res10-notas5*5


    print("{0} dolars equals to {1}€ (with cents={2} )".format(valDolar,valEuro,(valDolar*rate)))
    print("so you will recieve {0} 50€ notes, {1} 20€ notes, {2} 10€ notes, {3} 5€ notes and you will recieve {4}€ in coins".format(notas50,notas20,notas10,notas5,res5))
