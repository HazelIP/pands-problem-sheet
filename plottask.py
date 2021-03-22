# The program displays a plot of the functions 
# f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.
# Some marks will be given for making the plot look nice.
# author: Ka Ling Ip

import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array (range(0,4)) #f(x)
ypoints = xpoints * xpoints #g(x) = x squared
zpoints = xpoints * xpoints * xpoints # h(x) = x cubed

#plt.plot (xpoints, ypoints, zpoints) # create a plot showing the functions
plt.plot (xpoints, ypoints, 'b', zpoints, 'y')
plt.title("Display functions g(x), h(x)")
plt.legend()
plt.show()