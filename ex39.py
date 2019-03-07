from random import randint
def main():
    horario=[]
    programa=[]
    dia=input("Qual o dia da semana: ")
    estacao=input("Qual a estacao: ")
    fim=False
    i=0
    prog=""
    hor=""
    while fim==False:
        prog=input("Qual o programa a inserir: ")
        hor=input("Qual o horario (insira a hora de inicio e fim no seguint formato e separado por espaços [hh:mm hh:mm])")
        programa.append(prog)##não esquecer
        horario.append(hor)##não esquecer
        i+=1
        if int(input("Quer terminar [0-nao|1-sim]: ")) == 1:
            fim=True
    print("")
    print("")
    print("")
    print("Na/no {0} a estação {1} irá transmitir o seguinte: ".format(dia,estacao))
    print("------------------------------------------------")
    for count in range(0,i):
        print("{0:^10} | {1:^10}".format(programa[count],horario[count]))
    print("------------------------------------------------")
