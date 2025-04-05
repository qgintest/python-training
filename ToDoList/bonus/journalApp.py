
filename = input("Enter Today's date: ")
filename = filename + ".txt"

mood = input("How do you rate your mood from 1 - 10? ")
entry = input("Let your thoughts flow:\n")



with open(filename, 'w') as file:
    file.write(mood + 2 * "\n")
    file.write(entry + 2 * "\n")

with open(filename) as file:
    entries = file.readlines()
    for entry in entries:
        print(entry)
