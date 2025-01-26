### Simple Uniswap V3 concentrated liquidity implementation (only the mathematical part)

> Understanding Uniswap v3 is kind of hard compared to v1 and v2; there's like a lot of magical black box formulas that do "stuff." I kind of made this after trying to figure out how Uniswap v3 works under the hood after 
 reading the Uniswap v3 book and other resources. Note that if there are any issues or something is not mathematically correct, please issue a pull request; I'm still learning on the learning curve... so yk...

- Initializing a new curve in tests.py with:

```python
curve = curve.BondingCurve(50000, 50000, 1, 7, 0.5)
```

#### BondingCurve(amountTokenX, amountTokenY, currentPrice, upperPrice, lowerPrice)

As we can see that the above curve is not so capital efficient due to the far price limits...

--- 

A simple swap of 1522 token x for token y:

<p float="left">
  <img src="https://github.com/pvnotpv/bonding-curve-plotter/blob/main/images/eqs.png?raw=true" width="700" />
</p>

The plotted graph for above swap:

<p float="left">
  <img src="https://github.com/pvnotpv/bonding-curve-plotter/blob/main/images/curve1.png?raw=true" width="800" />
</p>

---

Files:

```curve.py``` - The main curve class which defines all the parameters and methods.

```graph.py``` - Used to plot the curve.

```tests.py``` - For swapping tokens and saving the state to state.json

```swap.py``` - Does the actual swapping part.

---

The "tests.py" file accepts two arguments (xOry, amount):

xOry = 1, when swapping token y for token x

xOry = 0, when swapping token x for token y

---
- tests.py dumps the current state of the curve to a json file.

- Running ```graph.py scale``` will take the current state from state.json and plots the graph.

- The graph.py accepts a scale variable that is used to scale the graph... Since there can be a lot of scenarios... I really have no idea how to do it programmatically, but this way gives you a lot of control of the plotted graph; you can make it look beautiful, tbh.

Use cases and different scenarios explained in my blog post: 
