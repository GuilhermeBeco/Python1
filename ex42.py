def main():
    lista=[]
    i=0
    j=0
    temp=""
    fim=False
    fimM=False
    str=""
    opt=-1
    optDlt=5
    dlt=-1
    keep=True
    kGoing=-1
    while fimM==False:
        print("1: Inserir item à lista")
        print("2: Ordenar a lista")
        print("3: Apresentar a lista")
        print("4: Remover da lista")
        print("0: Sair")
        opt=int(input("Qual é a sua opcao: "))
        if opt==1:
            while fim==False:
                str=input("Insira o item da lista (para terminar apenas carrega no 'enter'): ")
                if str == "":
                    fim=True
                else:
                    lista.append(str)##não esquecer
                    i+=1
        elif opt==2:
            #bsort
            trocas=False
            while not trocas :
                trocas=True
                for counter in range (0,i-1):
                    if lista[counter]> lista[counter+1]:
                        trocas=False
                        temp=lista[counter]
                        lista[counter]=lista[counter+1]
                        lista[counter+1]=temp
            #bsort

        elif opt==3:
            print(lista[0:i])
        elif opt==4:
            optDlt=int(input("Pretende eliminar toda a lista (0) ou algum/ns intem/ns da lista(1): "))
            if optDlt==0:
                lista=[]
                print("Lista apagada")
            else:
                while keep==True:
                    for val in lista:
                        print("{0} - {1}".format(j,val))
                        j+=1
                    dlt=int(input("Qual o item que pretende eliminar: "))
                    if dlt>i-1 or dlt<0:
                        print("Objecto inválido")
                    else:
                        lista.pop(dlt)
                    kGoin=int(input("Pretende continuar a eliminar (0-nao|1-sim): "))
                    if kGoin==0:
                        keep=False
                    else:
                        j=0
                    if not lista:
                        print("Lista apagada")
                        keep=False
        elif opt==0:
            fimM=True
        else:
            print("Opt inválida")
