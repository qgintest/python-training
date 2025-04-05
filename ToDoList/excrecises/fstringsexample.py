filenames = ['document', 'report', 'presentation']

for index, filename in enumerate(filenames):
    print(f"{index}-{filename.title()}.txt")


# 0-Document.txt
#
# 1-Report.txt
#
# 2-Presentation.txt

# iterate over all characters of a string and assign an index value to each string
for i, j in enumerate('Gashe'):
    print(i+1, j)


    # enumerate is a list of tuples