import random
def main():
    jogo = []
    for column in range(7):
        jogo.append([])
        for row in range(6):
            jogo[column].append("O")

            ##cria a matriz (insere primeiro um array e depois de esse array insere os '0' dentro do array inserido


    players = []
    for player in range(2):
        tempPlayer = input("Please enter your name: ")
        players.append(tempPlayer)
        #um array para os players de modo a saber qual será e para a seguir fazer o random e dar as cores

    if (random.randint(1, 10) % 2) == 0:
        startPlayer = 0
    else:
        startPlayer = 1

    print()
    print("{0} you get to start!".format(players[startPlayer]))
    #random do player que começa

    token = input("Whould you like to play as (R)ed or (Y)ellow: ")
    if token == "R":
        tokens = ["R", "Y"]
    else:
        tokens = ["Y", "R"]

    #insert de cores

    win = False
    for count in range(0,7):
        jogo.append("0 0 0 0 0 0 0")

    while not win:
        print()
        print("The jogo currently looks like this: ")
        print()
        for row in range(6):
            for column in range(7):
                if column < 6:
                    print("{0} ".format(jogo[column][row]), end=" ")
                else:
                    print("{0}".format(jogo[column][row]))
                #print do jogo sendo que verifica se é a ultima coluna para quebrar a linha
        print()
        print("A  B  C  D  E  F  G")
        print()

        print("It is {0}'s turn...".format(players[startPlayer]))
        shot = input("Which column do you want to place a counter in: ")
        #obtem a opção de jogo
        if shot == "A":
            played = False  #para saber se a jogada foi feita
            counter = 5 #começa de baixo para cima!!!!
            while not played and counter >= 0:
                if jogo[0][counter] == "O": #é para saber em qual linha da coluna A irá colucar
                    jogo[0][counter] = tokens[startPlayer] #coloca na coluna certa
                    played = True #jogada feita
                else:
                    counter = counter - 1 #senão decrementa o contador

        elif shot == "B":
            played = False
            counter = 5
            while not played and counter >= 0:
                if jogo[1][counter] == "O":
                    jogo[1][counter] = tokens[startPlayer]
                    played = True
                else:
                    counter = counter - 1
        elif shot == "C":
            played = False
            counter = 5
            while not played and counter >= 0:
                if jogo[2][counter] == "O":
                    jogo[2][counter] = tokens[startPlayer]
                    played = True
                else:
                    counter = counter - 1
        elif shot == "D":
            played = False
            counter = 5
            while not played and counter >= 0:
                if jogo[3][counter] == "O":
                    jogo[3][counter] = tokens[startPlayer]
                    played = True
                else:
                    counter = counter - 1
        elif shot == "E":
            played = False
            counter = 5
            while not played and counter >= 0:
                if jogo[4][counter] == "O":
                    jogo[4][counter] = tokens[startPlayer]
                    played = True
                else:
                    counter = counter - 1
        elif shot == "F":
            played = False
            counter = 5
            while not played and counter >= 0:
                if jogo[5][counter] == "O":
                    jogo[5][counter] = tokens[startPlayer]
                    played = True
                else:
                    counter = counter - 1
        elif shot == "G":
            played = False
            counter = 5
            while not played and counter >= 0:
                if jogo[6][counter] == "O":
                    jogo[6][counter] = tokens[startPlayer]
                    played = True
                else:
                    counter = counter - 1

        #o mesmo commentário da A, aplica-se para o resto
        # check to see if currentplayer has won vertically
        connect = 0
        for each in jogo:#percorre as colunas
            for item in each:#percorre cada elemento da coluna
                if item == tokens[startPlayer]:#verifica se está lá o token
                    connect = connect + 1 #se estiver dá incremento
                else:
                    connect = 0
                if connect == 4:#se o incremento chegou a 4, então o jogador venceu
                    win = True
         # check to see if currentplayer has won horizontally
        connect = 0
        for row in range(6):#percorre as linhas
           for column in range(7):#percorre cada
               if jogo[column][row] == tokens[startPlayer]:#verifica se a linha e coluna tem o token
                    connect = connect + 1#se tiver dá incrment
               else:
                    connect = 0
               if connect == 4:#se o increment chegar a 4 o player venceu
                 win = True

        # switch to next player
        if not win:#se o jogo não acabrou
            if startPlayer == 0:#obtem qual o player que está em jogo
                startPlayer = 1#muda o jogador
            else:
                startPlayer = 0
        # game won
    print()
    print("The final board: ")
    print()
    for row in range(6):
        for column in range(7):
            if column < 6:
                print("{0} ".format(jogo[column][row]),end=" ")
            else:
                print("{0}".format(jogo[column][row]))
    # print do jogo sendo que verifica se é a ultima coluna para quebrar a linha
    print()
    print("A  B  C  D  E  F  G")
    print()
    print("{0} you connected 4 - well done!".format(players[startPlayer])) #informa o player que venceu