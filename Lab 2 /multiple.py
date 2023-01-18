import matplotlib.pyplot as plt   #import modules 
import numpy as np
import time
startime = time.time() #we start the timer at start of code
array = [ ]  #create an empty list for the number of iterations 
def collatz(n): #defining collatz function to process different integer values ranging from 1 to 1000000
    i = 0 
    while n!=1:
        if n % 2 == 0:
            n = n//2
        else: 
            n = (3*n+1)
        i+=1
    return i #returning the number of iterations it takes any number between 1 and 1000000
for x in range(1000000):
    array.append(collatz(x+1)) #looping through different integer values from 1 to 1000000
plt.plot (range (1,1000001),array) #plotting integers from 1 to 1000000 vs. the number of iterations 
plt.xscale("log") #making x axis a log scale 
plt.xlabel('log10(n)')  #naming x and y axis 
plt.ylabel('C(n)')
plt.show() #printing plot 
max_iterations = (max(array)) #finding the maximum number of iterations 
max_number = (np.argmax(array)+1) #finding the integer assoicted with the 
endtime = time.time() #ending timer 
t = endtime - startime #time it took to complete loops for all integers ranging from 1 to 1000000 
print("The time that it took the run the program was {} seconds. Additonally, the number with the largest amount of iterations is {} taking {} iterations".format(t,max_number,max_iterations))