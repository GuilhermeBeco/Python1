def insertionSort(lista,first,last):
    count=0
    for i in range(first+1,last):
        valorAtual=lista[i]
        ponteiro=i-1
        while lista[ponteiro]>valorAtual and ponteiro>=0:
            count+=1
            lista[ponteiro+1]=lista[ponteiro]
            ponteiro-=1
        lista[ponteiro+1]=valorAtual
    print ("Foram feitas {0} comparaçoẽs".format(count))
    return lista
def main():
    lists = [9, 1, 5, 4, 10, 7, 3,6, 2, 8]
    print(lists)
    lists = insertionSort(lists,0,len(lists))
    print (lists)