def times(num):
    for counter in range(1,10):
        res=counter*num
        print("{0:^3} * {1:^4} = {2:^4}".format(num,counter,res))
        #print("{0} * {1} = {2}".format(num,counter,res))
def main():
    vezes=int(input("Qual o numero que pretende fazer a tabuada: "))
    times(vezes)

