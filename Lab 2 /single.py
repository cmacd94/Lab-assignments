n = int(input(f" Please insert an integer: ")) #input the the integer you want to use 
def collatz(n):
    i = 0  #number of iterations start at zero 
    while n!=1:   # while loop if the number isn't 1 it goes through loop, then terminates when it equals 1 
        if n % 2 == 0:  #if number is even, divide by 2 
            n = n//2
        else: #if not even (odd), times by 3 and add 1
            n = 3*n+1 
        print (n)  #we then print the result for each outputted number from original inputted number until loop terminates on 1 
        i += 1   #after each cycle in loop, add 1 to i 
    print("It took {} iterations to reach 1".format(i)) #print out the number of iterations 
collatz(n)

