# The program displays a plot of the functions, 
# f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.
# author: Ka Ling Ip

import numpy as np
import matplotlib.pyplot as plt

f = np.array ([0,1,2,3,4]) #f(x) in range [0,4]
g = f * f #g(x) = f squared
h = f * f * f # h(x) = f cubed
 
# create a plot showing the 3 functions, with lines of different colors ref[8.1]
plt.plot (f,'r', linewidth = '3', label = 'f(x)') #f(x) in red line
plt.plot (g,'b', linewidth = '3', label = 'g(x)') #g(x) in blue line
plt.plot (h,'y', linewidth = '3', label = 'h(x)') #h(x) in yellow line
plt.title("Functions f(x), g(x), h(x)") # ref[8.2]
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend(loc="upper left")
plt.show()

#ref[8.1]: https://www.w3schools.com/python/matplotlib_line.asp
#ref[8.2]: https://www.w3schools.com/python/matplotlib_labels.asp