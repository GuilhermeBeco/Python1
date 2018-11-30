import math
def main():
    grausNorte=int(input("A quantos graus está do norte: "))
    grausEste=90-grausNorte
    distancia=float(input("Qual a distancia que o aviao já percorreu: "))
    distanciaEste=grausEste*20
    distanciaNorte=grausNorte*20
    print("O aviao está a {0}km de este e a {1}km graus de norte"
    .format(distanciaEste,distanciaNorte))
