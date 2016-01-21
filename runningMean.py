import numpy as np

def running_mean(x, N):
	meanList = np.zeros(len(x))
	for y in range(len(x)):
		tempList = np.zeros((N*2)+1)
		tempList[N] = x[y]
		for z in range(1, N+1):
			if(y-z)<0:
				p = len(x)-np.abs(y-z)
			else:
				p = y-z
			if(y+z)>=len(x):
				q = y+z-len(x)
			else:
				q = y+z
			tempList[N-z] = x[p]
			tempList[N+z] = x[q]
		print(tempList)
		meanList[y] = np.mean(tempList)
	print()
	return meanList

x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
print("X is: " + str(x))
print("Running mean with N = 2: " + str(running_mean(x, 2)))


