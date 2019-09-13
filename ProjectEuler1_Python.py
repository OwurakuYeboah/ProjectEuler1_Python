#This program solves Problem 1 of Project Euler which is:
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.


eulerSolution = 0   # Variable to hold solution

for i in range(0, 1000):    # Loop through numbers below 1000
    #Add number to variable if it is a multiple of 3
    if i % 3 == 0:
        eulerSolution = eulerSolution + i
    #Add number to variable if it is a multiple of 5
    elif i % 5 == 0:
        eulerSolution = eulerSolution + i

#Print results
print("PROJECT EULER PROBLEM 1 SOLUTION")
print("The sum of multiples of 3 and 5 below 1000 is", eulerSolution)






