# convert feet and inches to meters

feet_inches = input('Enter Feet and Inches: ')

def parse(feetinchces):
    parts = feet_inches.split(' ')
    feet = float(parts[0])
    inches = float(parts[1])
    return feet, inches


def convert(feet, inches):
    meters = (feet * 0.3048) + (inches * 0.0254)
    print(meters)
    return meters
    #return f"{feet} feet and {inches} inches is equal to {meters} meters"


feet_inches_tuple = parse(feet_inches)
f, i = parse(feet_inches) # implicitely returns a tuple and assigns to f and i

print("fi" , feet_inches_tuple)
#result = convert(feet_inches_tuple[0], feet_inches_tuple[1])
result = convert(f, i)

if result < 1:
    print('Teeny Weeny')
else:
    print('You a big boyy')
