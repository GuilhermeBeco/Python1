import math
def main():
    valDolar=float(input("Insert the amount to convert: "))
    rate=0.88
    valEuro=int(valDolar*rate)
    print("{0} dolars equals to {1}€ (with cents={2} )".format(valDolar,valEuro,(valDolar*rate)))
