


from pet import Pet
import csv
def menu():
    
    print('''1.	Read pet information from file\n
 2.	Ask user for number of new pets they want to enter\n
 3.	write ALL pet information into ANOTHER file\n
 4.	Exit\n''')
    
def read(pets):
    
    with open('pets.csv','r') as file:
    
        
        # iterate over rows

        next(file)
        file = csv.reader(file)
        #skip first row
        for row in file:
            
            
            # extract cell content to variables
            name = row[0]
            age = row[1]
            pType = row[2]
            # create instance
            
            p_instance = Pet(name, age, pType)
            
            # add to list
            pets.append(p_instance)
        return pets

def new_info(pets):
    
    num = int(input("Enter number of pets: "))
    
    
    for x in range(1,num+1):
        
        print("Enter Info for Pet #" + str(x))
        
        name = input("Enter name: ")
        age = int(input("Enter Age: "))
        pType = input("Enter Pet Type: ")
        
        # create instance
        instance = Pet(name,age,pType)
        
        # append instance to list
        pets.append(instance)
    return pets

def write_info(pets):
    
    # write instance into csv file named updated_pets
    
    with open('updated_pets.csv','w', newline='') as outFile:
        
        # call the writer
        outFile = csv.writer(outFile)
        
        # write a header row
        
        outFile.writerow(['Name','Age','Pet Type'])
        
        # iterate over list of instances and write to file
        
        for instance in pets:
            
            outFile.writerow([instance.get_name(), instance.get_age(), instance.get_type()])
    
