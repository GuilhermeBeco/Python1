from random import randint
def main():
    lista=[]
    i=0
    temp=""
    fim=False
    str=""
    while fim==False:
        str=input("Insira o item da lista (para terminar apenas carrega no 'enter'): ")
        if str == "":
            fim=True
        else:
            lista.append(str)##não esquecer
            i+=1
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


    print(lista[0:i])
