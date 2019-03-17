def main():
    nomes=["Beco", "Gui","Natalia","Gabriela"]
    with open("nomes.txt",mode="w",encoding="utf-8") as nomesFile:
        for nome in nomes:
            nomesFile.write(nome+"\n")
