import numpy as np
import matplotlib.pyplot as plt
import math as math
import matplotlib.mlab as mlab





size = 10
n_p = np.zeros((2,1))
grid = np.zeros((2*size+1,2*size +1),dtype = int)
for i in range(1,size):
	k = np.size(n_p[0,:])
	n = np.zeros((2,9*k))
	index = 0
	for j in range(k):
		n[0,index]   = n_p[0,j]+1
		n[0,index+1] = n_p[0,j]+1
		n[0,index+2] = n_p[0,j]-1
		n[0,index+3] = n_p[0,j]-1
		n[0,index+4] = n_p[0,j]
		n[0,index+5] = n_p[0,j]+1
		n[0,index+6] = n_p[0,j]
		n[0,index+7] = n_p[0,j]-1
		n[0,index+8] = n_p[0,j]

		n[1,index]   = n_p[1,j]+1
		n[1,index+1] = n_p[1,j]-1
		n[1,index+2] = n_p[1,j]+1
		n[1,index+3] = n_p[1,j]-1
		n[1,index+4] = n_p[1,j]
		n[1,index+5] = n_p[1,j]
		n[1,index+6] = n_p[1,j]+1
		n[1,index+7] = n_p[1,j]
		n[1,index+8] = n_p[1,j]-1
		index += 9
	n_p = n
	
print(n)
for i in range(np.size(n[0,:])):
	x = int(n[0,i])
	y = int(n[1,i])
	grid[x,y] += 1;

size = int(np.max(n[0,:]))
x = np.arange(-size,size+1,2,dtype = int)
print(x)
print(n[0,0])
xv,yv = np.meshgrid( x,x)




print(grid)
plt.scatter(xv,yv,c = grid[xv,yv],cmap = 'YlOrBr',s =100)
plt.show()
