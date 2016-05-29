from matplotlib import pyplot as plt
import numpy as np
from math import sqrt

def getFeatures(path):

		file = open(path, "r")
		data = [float(i) for i in file.read().split()]
		x = []
		y = []
		z = []

		## data loading ###
		for i in range(len(data)):
			if(i%4==(3)):
				continue
			else:
				if(i%4==0):
					x.append(data[i])
				elif(i%4==1):
					y.append(data[i])
				else:
					z.append(data[i])
		
		length = min(len(x),len(y),len(z))
		x = x[:length]
		y = y[:length]
		z = z[:length]	
		## dynamic threshhold truncation ##

		sx,sy,sz = np.std(x),np.std(y),np.std(z)

		dalpha = 0.2
		dx = dalpha *  sqrt(sx)
		dy = dalpha * sqrt(sy)
		dz = dalpha * sqrt(sz)

		maxIdx = -1
		minIdx = len(x)

		for i in range(len(x)):
			if x[i]<=dx and x[i]>=(-dx):
				maxIdx = max(maxIdx,i)
			else:
				break

		for i in range(len(y)):
			if y[i]<=dy and y[i]>=(-dx):
				maxIdx = max(maxIdx,i)
			else:
				break

		for i in range(len(z)):
			if z[i]<=dz and z[i]>=(-dz):
				maxIdx = max(maxIdx,i)
			else:
				break


		for i in range(len(x)-1,-1,-1):
			if x[i]<=dx and x[i]>=(-dx):
				minIdx = min(minIdx,i)
			else:
				break

		for i in range(len(y)-1,-1,-1):
			if y[i]<=dy and y[i]>=(-dy):
				minIdx = min(minIdx,i)
			else:
				break


		for i in range(len(z)-1,-1,-1):
			if z[i]<=dz and z[i]>=(-dz):
				minIdx = min(minIdx,i)
			else:
				break

		x = x[maxIdx+1:minIdx]
		y = y[maxIdx+1:minIdx]
		z = z[maxIdx+1:minIdx]

		## dynamic threshhold tructation done ##

		# smoothify alomng the 3 axes #
		alpha = 0.3
		prev = 0
		for i in range(len(x)):
			xx = x[i]
			yy = alpha*prev + (1-alpha)*(x[i-1])
			x[i] = yy
			prev = xx

		prev = 0	
		for i in range(len(y)):
			xx = y[i]
			yy = alpha*prev + (1-alpha)*(y[i-1])
			y[i] = yy
			prev = xx

		prev = 0
		for i in range(len(z)):
			xx = z[i]
			yy = alpha*prev + (1-alpha)*(z[i-1])
			z[i] = yy
			prev = xx
                 
		#print("temp x, y, z", x+y+z[:50])
		return x,y,z

def buildImg(x,y,z):
		result = []
		print len(x),len(y),len(z)
		for i in range(len(x)):
			temp = []
			temp.append(x[i])
			temp.append(y[i])
			temp.append(z[i])
			result.append(temp)
		return result

