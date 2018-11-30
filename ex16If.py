def main():
    age=int(input("Qual a sua idade: "))
    if age>=18:
        print("Pode votar")
    else:
        print("Não pode votar")
    retire=65-age
    print("Pode-se reformar daqui a {0} anos".format(retire))
