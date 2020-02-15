import numpy as np
import matplotlib.pyplot as plt
import random
import pickle
from Data import data


def show_pizza_output(data:  data):
    out = np.zeros((data.y,data.x, 3))
    for s in data.slices:
        (x0, x1, y0, y1) = s
        s_color =  [max(0.02,random.random()-0.1), max(0.1,random.random()-0.1), max(0.1,random.random()-0.1)]
        for x in range(x0, x1+1):
            for y in range(y0, y1+1):
                out[y][x] = s_color
    plt.imshow(out)
    plt.show()

if __name__ == '__main__':

    with open("object", "rb") as f:
        data = pickle.load(f)
    show_pizza_output(data)
