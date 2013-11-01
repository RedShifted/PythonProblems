# mandelbrot set by sdbonin

from __future__ import division # make division not stupid

# import functions
from scipy import zeros
import matplotlib.pyplot as plt
from matplotlib import *
from pylab import *

matplotlib.pyplot.close("all") # close any open plots

# define range, resolution, and number of iterations
xmax = 1
xmin = -2.5
iymax = 1
iymin = -1
xres = 1600
iyres = 900
iter = 100

xspace = linspace(xmin,xmax,xres+1)
yspace = linspace(iymin,iymax,iyres+1)
xgran = abs(xspace[1]-xspace[2])
ygran = abs(yspace[1]-yspace[2])

count = 0
totalpixils = size(xspace)*size(yspace)

fracmat = zeros((size(yspace),size(xspace))) # preallocate array
zplane = zeros((size(yspace),size(xspace)),dtype=complex)

# compute fractal
for row in range(0,size(yspace)):
    for col in range(0,size(xspace)):
       z = (xmin+xgran*col)+(iymax-ygran*row)*1j
       zplane[row,col] = z # debug with coordinate plane
       c = (xmin+xgran*col)+(iymax-ygran*row)*1j
       for k in range(1,iter):
           z = z**2 + c
           iteration = k
           if (z.real**2 + z.imag**2) > 4:
               break
       count = count+1
       perdone = (count/totalpixils)*100
       print perdone,"%"
       fracmat[row,col] = iteration # the fractal
       

fig=plt.figure()
ax = plt.axes([0,0,1,1])
mdblt = plt.imshow(flipud(fracmat)) # define plot
plt.axis('off')

plt.savefig('mandelbrot.jpg',bbox_inches='tight',pad_inches=0)
plt.show() # show plot