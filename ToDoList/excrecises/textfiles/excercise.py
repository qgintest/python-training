contents = ['content one', 'content 2', 'content 3']

filenames = ['doc.txt', 'report.txt', 'presentation.txt']


# Below method works, pretty similar to java

# fileSize = len(filenames)
# index = 0
# for content in contents:
#     file = open(filenames[index], 'w')
#     file.writelines(contents[index])
#     file.close()
#     index = index + 1

# Below is alternative specific to Python
for content, filename in zip(contents, filenames):
    file = open(f"files/{filename}", 'w')
    file.writelines(content)
    file.close()


