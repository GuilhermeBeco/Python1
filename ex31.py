def main():
    string=input("Qual a string que pretende verificar: ")
    char=input("Qual o char que pretende verificar: ")
    strlen=len(string)
    stringSem=""
    contador=0
    for counter in range(0,strlen):
        if string[counter] == char :
            contador=contador+1
            stringSem=stringSem+string[counter]
        else:
            stringSem=stringSem+'_'
            #"".join(stringSem)
    if contador==0:
        print("A sua string '{0}' não contem o char '{1}'".format(string,char))
        ##print("A sua string '{0}' não contem o char '{1}'".format(string,char))
    else:
        print("A sua string '{0}' e contem o char '{1}' exatas {2} vezes".format(stringSem,char,contador))
