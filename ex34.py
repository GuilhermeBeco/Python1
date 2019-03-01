def main():
    words = ["sun","hi","say","hello","world"]
    letter="s"
    word=""
    numWords=0
    for counter in range(0,len(words)):
        word=words[counter]
        if word[0]==letter:
            print(word)
            numWords=numWords+1
    print("O numero de palavras começadas por {0} são {1}".format(letter,numWords))
