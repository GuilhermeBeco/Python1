from random import randint
def main():
    lista=[]
    i=0
    fim=False
    str=""
    while fim==False:
        str=input("Insira o item da lista (para terminar apenas carrega no 'enter'): ")
        if str == "":
            fim=True
        else:
            lista.append(str)##não esquecer
            i+=1


    print(lista[0:i])
