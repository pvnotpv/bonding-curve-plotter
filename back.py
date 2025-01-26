import matplotlib.pyplot as plt
import numpy as np
import json

with open('stat.json', 'r') as f:
    data = json.load(f)

k = data["k"]

xpoints = np.arange(0, 250000, 1000)
ypoints = []

for i in xpoints:
    y = k/i
    ypoints.append(y)

current_price = []
for i in xpoints:
    current_price.append(i)

upper_price = []
for i in xpoints:
    upper_price.append(data["priceUpper"]*i)

lower_price = []
for i in xpoints:
    lower_price.append(data["priceLower"]*i)

plt.xlim(0, 250000)
plt.ylim(0, 250000)

plt.plot(xpoints, ypoints)
plt.plot(xpoints, current_price)
plt.plot(xpoints, upper_price)
plt.plot(xpoints, lower_price)

plt.scatter([data["x"]], [data["y"]], color='red', label="Special Point", zorder=5)

#plt.axvline(x=data["x"], color='green', linestyle='-', label=f'Vertical Line at x={data["x"]}')
#plt.axhline(y=data["y"], color='blue', linestyle='-', label="Horizontal Line at y=0")

#plt.axvspan(70000, 90000, color='yellow', alpha=0.3, label="Highlighted Region")

plt.legend()

plt.show()
