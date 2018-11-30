def main():
    frase=input("Indique a frase: ")
    frase.replace("a","o")
    print("Frase em caps: {0} Frase em lower: {1} "
    "Frase capitalizada: {2} Frase em titulo: {3}".format(frase.upper(),frase.lower(),frase.capitalize(),frase.title()))
