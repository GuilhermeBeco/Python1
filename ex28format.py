def main():
    vezes=int(input("Qual o numero que pretende fazer a tabuada: "))
    for counter in range(1,10):
        res=counter*vezes
        print("{0:^4} * {1:^2} = {2:^4}".format(vezes,counter,res))
