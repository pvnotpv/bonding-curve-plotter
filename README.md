### Simple Uniswap V3 concentrated liquidity implementation (only the mathematical part)

> Understanding Uniswap v3 is kind of hard compared to v1 and v2; there's like a lot of magical black box formulas that do "stuff." I kind of made this after trying to figure out how Uniswap v3 works under the hood after 
 reading the Uniswap v3 book and other resources. Note that if there are any issues or something is not mathematically correct, please issue a pull request; I'm still learning on the learning curve... so yk...

A simple swap of token x for token y:
![eqs](https://github.com/user-attachments/assets/2c64e86b-c973-4625-acc0-cb5151530345)

The plotted graph for the swap:
![curve1](https://github.com/user-attachments/assets/ad881cfd-82e4-4c56-b5bf-e4be9bb83526)


Files:
```curve.py``` - The main curve class which defines all the parameters and methods.
```graph.py``` - Used to plot the curve.
```tests.py``` - For swapping tokens.

The "tests.py" file accepts two arguments (xOry, amount)

xOry = 1, when swapping token y for token x
xOry = 0, when swapping token x for token y
