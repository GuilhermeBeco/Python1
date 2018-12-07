import time
def main():
    for counter in range(10,-1,-1):
        if counter == 0:
            print("Estamos em {0:^2} segundos, faltam {1:^2}".format(counter,counter))
        else:
            print("Estamos em {0:^2} segundos, faltam {1:^2}".format(counter,counter-1))
        time.sleep(1)
