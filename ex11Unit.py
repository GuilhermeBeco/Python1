import math
def main():
    r=float(input("What's the raius: "))
    p=(r*2)*math.pi
    res=round(p,2)
    print("The perimter is ",format(res))
