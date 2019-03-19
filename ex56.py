def bbSort(lista):
    temp=""
    trocas = False
    count=0
    while not trocas:
        trocas = True
        for counter in range(0, len(lista) - 1):
            if lista[counter] > lista[counter + 1]:
                count+=1
                trocas = False
                temp = lista[counter]
                lista[counter] = lista[counter + 1]
                lista[counter + 1] = temp
    print ("Fez {0} trocas".format(count))
    return lista
def main():
    lists=[10,1,5,4,9,7,3.6,2,8]
    lists=bbSort(lists)
    print(lists)