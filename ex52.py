def ordenar(lista):
    temp=""
    trocas = False
    while not trocas:
        trocas = True
        for counter in range(0, len(lista) - 1):
            if lista[counter] > lista[counter + 1]:
                trocas = False
                temp = lista[counter]
                lista[counter] = lista[counter + 1]
                lista[counter + 1] = temp
    return lista
def main():
    nomes=[]
    with open("nomes.txt",mode="r",encoding="utf-8") as nomesFile:
        for nome in nomesFile:
            nomes.append(nome.rstrip("\n"))
    nomes=ordenar(nomes)
    with open("nomes.txt",mode="w",encoding="utf-8") as nomesOrdenados:
        for nome in nomes:
            nomesOrdenados.write(nome+"\n")