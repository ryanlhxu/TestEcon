"""
hw2: polynomial interpolation
"""


import numpy as np 
from numpy.linalg import solve
import matplotlib.pyplot as plt 

# Data pionts
xi = np.array([-1.,1,2])
yi = np.array([0,4.,3])


# matrix
A = np.array([[1,-1.,1],[1.,1,1],[1.,2,4]])
b = yi

# solve the system
c = solve(A, b)

print "The polynomial coefficients are:"
print c

# plot the resulting polynomial
x = np.linspace(-2, 3)
y = c[0]+c[1]*x +c[2]*x**2


plt.figure(1)  # open plot figure windows
plt.clf()   # clear figure
plt.plot(x,y,'b-') #connect points with a blue line

# add data points
plt.plot(xi,yi,'ro') # plot as red circles
plt.ylim(-4,8)

plt.title("Data points and interpolating polynomial")
plt.show()












