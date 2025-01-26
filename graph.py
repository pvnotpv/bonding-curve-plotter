import matplotlib.pyplot as plt
import math
import numpy as np
import json
import sys
from PIL import Image, ImageDraw, ImageFont

with open('state.json', 'r') as f:
    data = json.load(f)

k = data["k"]

scale = int(sys.argv[1]) 
print(k, scale)

xVirtualRangeX = np.arange(0, data["xVirtual"])
xVirtualRangeY = []

for i in xVirtualRangeX:
    y = k/i
    xVirtualRangeY.append(y)

xRealRangeX = np.arange(data["xVirtual"], data["x"])
xRealrangeY = []

for i in xRealRangeX:
    y = k/i 
    xRealrangeY.append(y)

yRealRangeX = np.arange(data["x"], (data["k"]/data["yVirtual"]))
yRealRangeY = []

for i in yRealRangeX:
    y = k/i
    yRealRangeY.append(y)

yVirtualRangeX = np.arange((data["k"]/data["yVirtual"]), scale)
yVirtualRangeY = []

for i in yVirtualRangeX:
    y = k/i
    yVirtualRangeY.append(y)

width = 11
height = 12  
plt.figure(figsize=(width, height))

plt.plot(xVirtualRangeX, xVirtualRangeY, label='X virtual', color='purple', linewidth=3)
plt.plot(xRealRangeX, xRealrangeY, label='X real', linewidth=3, color='orange')
plt.plot(yRealRangeX, yRealRangeY, label='Y real', linewidth=3, color='green')
plt.plot(yVirtualRangeX, yVirtualRangeY, label='Y virtual', linewidth=3, color='brown')

xpoints = np.arange(0, scale, 1000)

current_price = []
for i in xpoints:
    current_price.append(data["priceCurrent"]*i)

upper_price = []
for i in xpoints:
    upper_price.append(data["priceUpper"]*i)

lower_price = []
for i in xpoints:
    lower_price.append(data["priceLower"]*i)

plt.xlim(0, scale)
plt.ylim(0, scale)

plt.plot(xpoints, current_price, color='blue', linewidth=2)
plt.plot(xpoints, upper_price, color='black', linewidth=2)
plt.plot(xpoints, lower_price, color='red', linewidth=2)

currentPriceX = [data["x"]] 
currentPriceY = [data["y"]] 

upperPriceX = [data["xVirtual"]] 
upperPriceY = [data["k"]/data["xVirtual"]]

lowerPriceX = [(data["k"]/data["yVirtual"])]
lowerPriceY = [data["yVirtual"]] 

plt.scatter(upperPriceX, upperPriceY, color='magenta', label=f'UpperPrice: {data["priceUpper"]}', zorder=5)
plt.scatter(currentPriceX, currentPriceY, color='gray', label=f'CurrentPrice: {data["priceCurrent"]}', zorder=5)
plt.scatter(lowerPriceX, lowerPriceY, color='blue', label=f'LowerPrice: {data["priceLower"]}', zorder=5)

plt.legend()
plt.xlabel("x reserves", fontsize=20, labelpad=25)
plt.ylabel("y reserves", fontsize=20, labelpad=20)
plt.savefig('assets/custom_plot.png')  # Save the image


img = Image.open('assets/custom_plot.png')

I1 = ImageDraw.Draw(img)
font = ImageFont.truetype("assets/Arial.ttf", size=21)


I1.text((28, 15), f'X real: {data["xReal"]:.2f}', fill=(0, 0, 0), font=font)
I1.text((28, 50), f'X virtual: {data["xVirtual"]:.2f}', fill=(0, 0, 0), font=font)
I1.text((28, 85), f'X (real+virtual): {data["x"]:.2f}', fill=(0, 0, 0), font=font)


I1.text((458, 15), f'L: {math.sqrt(data["k"])}', fill=(0, 0, 0), font=font)
I1.text((458, 50), f'K: {data["k"]}', fill=(0, 0, 0), font=font)
I1.text((458, 85), f'Curve Equation:', fill=(0, 0, 0), font=font)
I1.text((350, 116), f'(X_real+X_virtual)*(Y_real+Y_virtual) = L²', fill=(0, 0, 0), font=font)



I1.text((780, 15), f'Y real: {data["yReal"]:.2f}', fill=(0, 0, 0), font=font)
I1.text((780, 50), f'Y virtual: {data["yVirtual"]:.2f}', fill=(0, 0, 0), font=font)
I1.text((780, 85), f'Y (real+virtual): {data["y"]:.2f}', fill=(0, 0, 0), font=font)


img.show() 
img.save("assets/custom_plot.png")
