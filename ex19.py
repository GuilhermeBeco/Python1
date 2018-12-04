def main():
    mes=int(input("Mes em numero [1-12]: "))
    if mes>=3 and mes <=5:
        print("Está na primavera")
    elif mes>=6 and mes <=8:
        print("Está no verão")
    elif mes>=9 and mes <=11:
        print("Está no outono")
    else:
        print("Está no inverno")

    if mes==2:
        print("o seu mes tem 28 dias")
    else:
        if mes<=7:
            flag=True
        else:
            flag=False
            
        if flag==True:
            if mes%2==1:
                print("O seu mes tem 31 dias")
            else:
                print("O seu mes tem 30 dias")
        else:
            if mes%2==0:
                print("O seu mes tem 31 dias")
            else:
                print("O seu mes tem 30 dias")
