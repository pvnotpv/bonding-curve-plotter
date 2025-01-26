import sys
import math
import curve
import swap
from colorama import init, Fore
import sys
import json

init(autoreset=True)

curve = curve.BondingCurve(50000, 50000, 1, 7, 0.5)

def dumpCurve(): 
    with open('state.json', 'r') as f:
        data = json.load(f)

    data["x"] = curve.x
    data["y"] = curve.y
    data["k"] = curve.k
    data["xReal"] = curve.xReal
    data["yReal"] = curve.yReal
    data["xVirtual"] = curve.xVirtual
    data["yVirtual"] = curve.yVirtual
    data["priceCurrent"] = curve.sqrtpC**2
    data["priceUpper"] = curve.pB
    data["priceLower"] = curve.pA

    with open('state.json', 'w') as f:
        json.dump(data, f, indent=4)



def printStats():     
    print(Fore.RED+"Current Price: ", curve.sqrtpC**2)
    print(Fore.RED+"pA: ", curve.pA)
    print(Fore.RED+"pB: ", curve.pB, "\n")

    print(Fore.BLUE+"X real: ", curve.xReal)
    print(Fore.BLUE+"Y real: ", curve.yReal)

    print(Fore.BLUE+"X virtual: ", curve.xVirtual)
    print(Fore.BLUE+"Y virtual: ", curve.yVirtual, "\n")

    print(Fore.GREEN+"X: ", curve.x)
    print(Fore.GREEN+"Y: ", curve.y)
    print(Fore.GREEN+"K: ", curve.k)
    dumpCurve()


def swaps(y_in):
    print("---"*18)
    print(Fore.MAGENTA+"\nPerforming swaping")

    if(int(sys.argv[1])==1):
        (x_new, y_new, price_next, price_diff) = swap.swap(curve, 1, y_in)
        print(Fore.MAGENTA+"Price diff: ", price_diff)
        print(Fore.MAGENTA+"Y in: ", y_new)
        print(Fore.MAGENTA+"X out: ", x_new, "\n")
    else:
        tempPrice = curve.sqrtpC
        (x_new, y_new, price_next) = swap.swap(curve, 0, y_in)
        print(Fore.MAGENTA+"Price diff: ", tempPrice-(curve.sqrtpC**2))
        print(Fore.MAGENTA+"Y out: ", y_new)
        print(Fore.MAGENTA+"X in: ", x_new, "\n")

def main():
    printStats()
    swaps(int(sys.argv[2]))
    printStats()


if __name__ == "__main__":
     main()
