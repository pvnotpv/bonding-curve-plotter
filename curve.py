import math

class BondingCurve:
    def __init__(self, amount_token0, amount_token1, currentPrice, upperPrice, lowerPrice):
        self.amount_token0 = amount_token0
        self.amount_token1 = amount_token1

        self.pC = currentPrice
        self.pA = lowerPrice
        self.pB = upperPrice

        self.sqrtpA = self.priceSqrt(lowerPrice)
        self.sqrtpB = self.priceSqrt(upperPrice)
        self.sqrtpC = self.priceSqrt(currentPrice)

        self.liq0 = self.liquidityX(amount_token0, self.sqrtpC, self.sqrtpB)
        self.liq1 = self.liquidityY(amount_token1, self.sqrtpA, self.sqrtpC)
        self.liq = int(min(self.liq0, self.liq1))

        self.xReal = self.calc_xReal(self.liq, self.sqrtpC, self.sqrtpB)
        self.yReal = self.calc_yReal(self.liq, self.sqrtpA, self.sqrtpC)

        self.xVirtual = self.liq/self.sqrtpB
        self.yVirtual = self.liq*self.sqrtpA

        self.x = self.xReal+self.xVirtual
        self.y = self.yReal+self.yVirtual
        self.k = self.x*self.y  

    def update_y_in_x_out(self, realAmountX, realAmountY, newPrice):
        self.xReal -= realAmountX
        self.yReal += realAmountY
        self.sqrtpC = newPrice
        self.pC = self.sqrtpC**2

        self.x = self.xReal+self.xVirtual
        self.y = self.yReal+self.yVirtual
        self.k = self.x*self.y 

    def update_x_in_y_out(self, realAmountX, realAmountY, newPrice):
        self.xReal += realAmountX
        self.yReal -= realAmountY
        self.sqrtpC = newPrice
        self.pC = self.sqrtpC**2

        self.x = self.xReal+self.xVirtual
        self.y = self.yReal+self.yVirtual
        self.k = self.x*self.y

    def priceSqrt(self, n):
        return math.sqrt(n)

    def liquidityX(self, amount, pA, pB):
        l = amount*( (pA*pB) / (pB-pA) )
        return l

    def liquidityY(self, amount, pA, pB):
        l = amount / (pB - pA)
        return l

    def calc_xReal(self, liq, pA, pB):
        amount = liq * ( (pB - pA) / (pA*pB) )
        return amount

    def calc_yReal(self, liq, pA, pB):
        amount = liq*(pB - pA)
        return amount

    def addLiqudity(self, xOry, amount):
        if(xOry):
            # TODO: implement
            pass
        else:
            lX = self.liquidityX(amount, self.sqrtpC, self.sqrtpB)
            y = self.calc_yReal(lX, self.sqrtpA, self.pC)
        
            self.xReal+=amount
            self.yReal+=y
            self.x = self.xReal+self.xVirtual
            self.y = self.yReal+self.yVirtual
            self.k = self.x*self.y
            self.liq = math.sqrt(self.k)

            self.xVirtual = self.liq/self.sqrtpB
            self.yVirtual = self.liq*self.sqrtpA

            print(y)


