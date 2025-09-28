#Solution 1 (using exponentiation)

num1 = int(input("Enter a number to find the square root: "))
sr = num1**0.5 #or num**(1/2)
print("The square root of", sr)

#Solution 2 (using math module)
import math
num = int(input("Enter a number to find the square root: "))
sr = math.sqrt(num) #using sqrt function from math module
print("The square root of", sr)
