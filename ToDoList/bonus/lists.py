# transform the following list below to the expected archive

filenames = ["1.doc", "1.report", "1.presentation"]

# filenames = [filename.replace('.', '-') + 'txt' for filename in filenames] #Shortcut way, longer version below

new_filenames = []

for filename in filenames:
    filename = filename.replace('.', '-')
    filename = filename.replace(filename, f"{filename}.txt")
    new_filenames.append(filename)


print(new_filenames)



# Dictionary of tuples
day_temperatures = {"morning": (67.0, 69.9, 68.2), "noon": (77.0, 79.9, 78.2),
                    "evening": (87.0, 89.9, 88.2)}