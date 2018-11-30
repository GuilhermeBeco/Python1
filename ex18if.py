def main():
    scoreBenfica=int(input("Quantos golos o SLB marcou: "))
    scorePorto=int(input("Quantos goloso FCP marcou: "))
    pontosBenfica=0
    pontosPorto=0
    if scoreBenfica == scorePorto:
        pontosPorto=1
        pontosBenfica=1
    elif scoreBenfica > scorePorto:
        pontosBenfica=3

    else:
        pontosPorto=3

    print("O SLB tem {0} pontos e o FCP tem {1} pontos".format(pontosBenfica,pontosPorto))
