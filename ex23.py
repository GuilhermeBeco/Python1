import datetime
def main():
    mes=int(input("Qual o mes "))
    dia=int(input("Qual o dia "))
    ano=int(input("Qual o ano "))

    stringPrint=''
    if dia==1 or dia == 21 or dia ==31:
        stringPrint=stringPrint+str(dia)+'st'
    elif dia==3 or dia==23:
        stringPrint=stringPrint+str(dia)+'rd'
    elif dia==2 or dia == 22:
        stringPrint=stringPrint+str(dia)+'nd'
    else:
        stringPrint=stringPrint+str(dia)+'th'

    month = datetime.date(ano, mes, dia).strftime('%B')

    stringPrint=stringPrint+' '+month+' '+str(ano)
    print(stringPrint)
