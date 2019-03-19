def linear(lista,item):
    position=0
    found=False
    while position<len(lista) and not found:
        if lista[position]==item:
            found=True
        position+=1
    print("Foram feitas {0} pesquisas".format(position))
    return found
def insert(lista,item,found):
    if not found:
        lista.append(item)
        print("O item {0} foi adicionado à lista".format(item))
    return lista
def printRes(found):
    if found:
        print("O item foi encontrado")
    else:
        print("O item não foi encontrado")
def main():
    found = False
    lista=["Hello","World","i'm","Here"]
    found=linear(lista,"Hello")
    printRes(found)
    insert(lista, "Hello", found)
    found=linear(lista,"kek")
    printRes(found)
    insert(lista,"kek",found)
    print(lista)
