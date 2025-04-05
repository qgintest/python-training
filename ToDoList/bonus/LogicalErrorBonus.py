try:
    width = float(input("Enter Rectangle Width: "))
    length = float(input("Enter Rectangle length: "))
    if width == length:
        exit('This is not a Rectangle')

    area = width * length
    print(area)

except ValueError:
    print('Please Enter a number')


