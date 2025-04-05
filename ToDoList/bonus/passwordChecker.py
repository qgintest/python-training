
# 1: password must be 8 characters
# 2: password contains at least one digit
# 3. has one upper case letter

new_password = input('Enter a new Password ')

results = {}

passLn = len(new_password)

if passLn >= 8:
    results["length"] = True
else:
    results["length"] = False

digit = False
for i in new_password:
    if i.isdigit():
        digit = True

results["hasDigit"] = digit

uPassword = False
for u in new_password:
    if u.isupper():
        uPassword = True

results["hasUpper"] = uPassword
print(results)


if all(results.values()):
    print('Password is Strong')
else:
    print('Password does not meet criteria for all requirements')



