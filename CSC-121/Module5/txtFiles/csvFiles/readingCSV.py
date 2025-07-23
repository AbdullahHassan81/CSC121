#CSV Files
import csv

with open('contacts.csv', 'r') as contacts:

    #reader method from the csv libary
    contacts = csv.reader(contacts)

    for row in contacts:

        name, num = row
        
        print(name, num)

    #read
    #readline()
    #readlines()