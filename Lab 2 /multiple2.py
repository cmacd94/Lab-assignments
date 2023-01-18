import matplotlib.pyplot as plt
import numpy as np
import time
startime = time.time()
array = [ ]
def collatz(n):
    i = 0
    while n!=1:     #same as previous file but the following is changed
        if n % 2 == 0:
            n = n//2
            i+=1   # if number if even, it is counted as one iteration 
        else:
            n = (3*n+1)/2 
            i += 2  #if it is odd, two iterations are combined to save time due to dividing by 2 now
    return i

for x in range(1000000):
    array.append(collatz(x+1))
plt.plot (range (1,1000001),array)
plt.xscale("log")
plt.xlabel('log10(n)')
plt.ylabel('C(n)')
plt.show()
max_iterations = (max(array))
max_number = (np.argmax(array)+1)
endtime = time.time()
t = endtime - startime
print("The time that it took the run the program was {} seconds. Additonally, the number with the largest amount of iterations is {} taking {} iterations".format(t,max_number,max_iterations))
#This new script is usually a second faster than the multiple.py script 