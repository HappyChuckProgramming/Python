import matplotlib.pyplot as plt
import time
import numpy



def plot_linear_eq(a, b, clr):
    x = list(range(-10, 11))
    y = [ (a*i + b) for i in x]
    plt.plot(x, y, label='linear', linestyle='-', color=clr)
    plt.grid()

#client code
# y = ax + b generic linear equation

# (i) y = 0
a = 0
b = 0
plot_linear_eq(a, b, 'r')
plt.show(block=False)
plt.pause(5)
plt.close()

# (ii) y = x
a=1
b=0
plot_linear_eq(a, b, 'b')
plt.show(block=False)
plt.pause(5)
plt.close()

# (iii) y = -x
a=-1
b=0
plot_linear_eq(a, b, 'g')
plt.show(block=False)
plt.pause(5)
plt.close()

# (iv) y = x + 1 - transposition 
a = 1
b = 1
plot_linear_eq(a, b, 'y')
plt.show(block=False)
plt.pause(5)
plt.close()

def plot_quadratic_eq(a, b, c, clr):
    x = list(range(-10, 11))
    y = [ (a*i**2 + b*i + c) for i in x]
    plt.plot(x, y, label='linear', linestyle='-', color=clr)


#client code
# y = ax2 + bx + c

# y = x2
a = 1
b = 0
c = 0
plot_quadratic_eq(a, b, c, 'r')
plt.show(block=False)
plt.pause(5)
plt.close()

# y = -x2
a = -1
b = 0
c = 0
plot_quadratic_eq(a, b, c, 'b')
plt.show(block=False)
plt.pause(5)
plt.close()
