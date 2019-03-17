def main():
    logs=[]
    user=False
    i=0
    with open("login.txt",mode="r",encoding="utf-8") as login:
        for line in login:
            logs.append(line.rstrip("\n"))
    username=input("Qual o username: ")
    password=input("Qual a pass: ")
    j=0
    for log in logs:
        if (i % 2)==0:
            if log==username:
                user=True
                if logs[j+1]==password:
                    print("Login com sucesso")
                else:
                    print("Password falhada")
        j+=1
    if not user:
        print("O username não exite")

