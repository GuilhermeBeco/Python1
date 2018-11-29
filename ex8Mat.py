import math
def main():
    xFri=float(input("Insert dimension x from fri "))
    yFri=float(input("Insert dimension y from fri "))
    zFri=float(input("Insert dimension z from fri "))
    xLift=float(input("Insert dimension x from lift "))
    yLift=float(input("Insert dimension y from lift "))
    zLift=float(input("Insert dimension z from lift "))

    volLift=xLift*yLift*zLift
    volFri=xFri*yFri*zFri
    volRes= volLift-volFri

    print("Lift volume = {0}, fridge colume = {1}, space remaining = {2}".format(volLift,volFri,volRes))
