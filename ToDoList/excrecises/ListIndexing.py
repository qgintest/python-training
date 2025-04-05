mylist = [1, 'two', 3.3]

print(type(mylist[0]))
print(type(mylist[1]))
print(type(mylist[2]))
print(mylist[0] == 1) # will print true

print(mylist.index('two')) # will print 1
print(mylist.index(1)) # will print zero because that is the index number for value 1
print(mylist.index(3.3)) # will print 2

# __ are used by pyhthon internally so below will replace index 0
mylist.__setitem__(0, '1')
# mylist[0] = '1' # does the same as the code above
print(mylist[0])