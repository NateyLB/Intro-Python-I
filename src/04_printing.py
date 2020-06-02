"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print("x is %2d, y is %2.1f, z is %s "%(x, y+.25448, z))

# Use the 'format' string method to print the same thing
string = "x is {ten}, y is {two}, z is {like}"
print(string.format(ten= x, two= (y+.25448), like = z))

# Finally, print the same thing using an f-string
print(f"x is {x}, y is {y+.25448}, z is {z}")