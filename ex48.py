def main():
    with open("animals.txt", mode="r", encoding="utf-8") as my_file:
        for line in my_file:
            #print(line) como lê o \n e não tem a função rstrip , o python dá add a mais um enter proprio do python daí o line.rstrip("\n")
            print(line.rstrip("\n"))