# Then, create a program that:
#
# 1. reads each text file and
#
# 2. prints out the content of each file in the command line.
#
# The expected output would be like the following:

files = ['a.txt', 'b.txt', 'c.txt']

for f in files:
    file = open(f"files/{f}", 'r')
    print(file.read())

    # read() gets entire content as a string
    # readline() reads single line including \n

