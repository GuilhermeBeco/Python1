def binary(lista,item):
    searchFail=False
    first=0
    last=len(lista)-1
    found=False
    count=0
    while not found and first<=last and not searchFail :
        count+=1
        midpoint=(first+last)//2
        if lista[midpoint]==item:
            found=True
      
        else:
            if first>last :
                searchFail=True

            else:
                if lista[midpoint]>item :
                    last=midpoint-1
                else:
                    first=midpoint+1
    if found:
        print("Item encontrado com {0} pesquisas".format(count))
    else:
        print("Item não encontrado com {0} pesquisas".format(count))
def main():
    item=8
    lista=[1,2,3,4,5,6,7,8,9,10]
    binary(lista,item)
    item=11
    binary(lista,item)
