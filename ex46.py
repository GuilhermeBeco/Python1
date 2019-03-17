
def inputData():
    string = input("Qual a string que pretende verificar: ")
    char = input("Qual o char que pretende verificar: ")
    inp=[string,char]
    return inp
def charChar(io):
    strlen = len(io[0])
    stringSem = ""
    contador = 0
    for counter in range(0, strlen):
        if io[0][counter] == io[1]:
            contador = contador + 1
            stringSem = stringSem + io[0][counter]
        else:
            stringSem = stringSem + '_'
            # "".join(stringSem)
    ret=[contador,stringSem]
    return ret

def main():
    io=inputData()
    check=charChar(io)
    if check[0]==0:
        print("A sua string '{0}' não contem o char '{1}'".format(io[0],io[1]))
        ##print("A sua string '{0}' não contem o char '{1}'".format(string,char))
    else:
        print("A sua string '{0}' e contem o char '{1}' exatas {2} vezes".format(check[1],io[1],check[0]))