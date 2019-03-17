def main():
    lista=[]
    with open("shopping.txt",mode="r",encoding="utf-8") as my_file:
        for line in my_file:
            lista.append(line.rstrip("\n"))
        #lista = my_file.read().splitlines() segunda opt
    print(lista[0:len(lista)])