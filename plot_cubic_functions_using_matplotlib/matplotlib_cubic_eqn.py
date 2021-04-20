import matplotlib.pyplot as plt
import time
import numpy


def plot_me(a, b, c, d, clr, mystr):
    x = numpy.arange(-3.0, 3.0, 0.05)
    y = [(a*i**3 + b*i**2 + c*i + d) for i in x]
    plt.plot(x, y, label='cubic', linestyle='-', color=clr)
    plt.grid(True)
    plt.text(2,4, mystr)
    plt.show(block=False)
    plt.pause(10)
    plt.close()

#client code
#(i) y = x**3
#General equation for a cubic fn -- y= ax3 + bx2 + cx + d
plot_me(1, 0, 0, 0, 'r', 'y = x**3')

#(ii) y = -x**3
plot_me(-1, 0, 0, 0, 'r', 'y = -x**3')

#(iii) y = x**3 - 4*x
plot_me(1, 0, -4, 0, 'r', 'y = x**3 - 4*x')

#(iv) y = -x**3 + 4*x
plot_me(-1, 0, 4, 0, 'r', 'y = -x**3 + 4*x')

#(v) y = x**3 -x + 8
plot_me(1, 0, -1, 8, 'r', 'y = x**3 -x + 8')

#(vi) y = -x**3 +x -8
plot_me(-1, 0, 1, -8, 'r', 'y= -x**3 +x -8')
