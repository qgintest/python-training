import csv

with open("weather.csv", 'r')as file:
    data = list(csv.reader(file))


city = input("Enter a country: ")

for row in data[1:]: # iterate row 1 to evertyhing to avoid column being read
    if row[0] == city:
    #print(row)
        print(row[1])


#print(data)