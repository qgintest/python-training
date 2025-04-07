# convert feet and inches to meters

feet_inches = input('Enter Feet and Inches: ')

def convert(feet_inches):
    parts = feet_inches.split(' ')
    feet = float(parts[0])
    inches = float(parts[1])

    meters = (feet * 0.3048) + (inches * 0.0254)
    print(meters)
    return meters
    #return f"{feet} feet and {inches} inches is equal to {meters} meters"


result = convert(feet_inches)

if result < 1:
    print('Teeny Weeny')
else:
    print('You a big boyy')
