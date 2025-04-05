# 1) uses list comprehension to capitalize all the names and surnames of the list, and
#
# (2) prints the updated list.

names = ["john smith", "jay santi", "eva kuki"]
names = [name.title() for name in names]
print(names)


# Extend the given code so the code prints out a list containing the number of characters for each username.
usernames = ["john 1990", "alberta1970", "magnola2000"]
usernames = [len(username) for username in usernames]
print(usernames)



#(1) converts the numbers from strings to floats, and
# (2) prints out the updated list.

user_entries = ['10', '19.1', '20']
user_entries = [float(user_entry) for user_entry in user_entries]
print(user_entries)


# (1) multiplies each number of the list by 2, and
#
# (2) prints out the updated list.
numbers = [10, 20, 30]
numbers = [number*2 for number in numbers]
print(numbers)


user_entries = ['10', '19.1', '20']
user_entries = [float(user_entry) for user_entry in user_entries]

# Solution 1 (longer way)
# previousUserEntry = float(0)
# for user_entry in user_entries:
#     previousUserEntry = previousUserEntry + user_entry
#
# print(previousUserEntry)


# Solution 2: shorter
print(sum(user_entries))