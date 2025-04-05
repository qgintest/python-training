filenames = ['1.item', '2.item', '3.item']

# example of changing parts of a string within a list without impacting other strings

print('before change', filenames)
for filename in filenames:
    filename = filename.replace('.', '-', 1)
    print(filename)


# tuples are created using ()
filenamesTuple = ('1.item', '2.item', '3.item')
tuple(filenamesTuple) # tuple
