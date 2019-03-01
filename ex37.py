from random import randint
def main():
    dado = [1,2,3,4,5,6]
    pontuacao=[0,0,0,0,0,0]
    for counter in range(0,30):
        pontuacao[randint(1,6)-1]+=1

    print(dado[0:6])
    print(pontuacao[0:6])
