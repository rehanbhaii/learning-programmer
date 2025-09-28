#Solution1 (using third variable)
x = 123
y = 456


tem = x #temporary variable to hold the value of x
x = y #assign the value of y to x
y = tem #assign the value of temporary variable to y
print("After swapping: x =", x)
print("After swapping: y =", y)