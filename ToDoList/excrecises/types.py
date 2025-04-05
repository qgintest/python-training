# number = 'a' + 10 # Runtime error, cannot add string to number
number = 5 * 'repeat5times'
print(number)

print(float(10.0)) # converts to a decimal
print(int('str')) # runtime error

xfloat = 10.1 # implicitely applies 10.1 as a float type
xinteger = 50 # implicitely applies 50 to a integer type
xstr = 'String of characters'

type(xfloat)
type(xinteger)
type(xstr)

str(10.1) # converts numbers/floats to string
