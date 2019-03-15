def inputData():
    return int(input("Qual o numero que pretende verificar: "))
def processData(number):
    div=number%7
    if div==0:
        return True
    else:
        return False
def outputData(res):
    if res:
        print("O numero é divisivel por 7")
    else:
        print("O numero não é divisivel por 7")
def main():
    outputData(processData(inputData()))