import classes.py

def main():

    #create the list 
    pets = []

    #loop iterates 3x for 3 pets 
    for i in range(3):

        #pet data 
        print("\nInfo for pet1",i)
        pet_name = input("Enter pet name: ") 
        pet_type = input("Enter pet type: ")
        pet_age = input("Enter pet age: ")

        #create the instance 
        mypet = classes.Pet(pet_name, pet_type, pet_age)

        #add instance to list 
        classes.append(mypet)

        #to displa info on lists of pets iterate over list of pets
        for item in pets:
            print()

            print(item)

#call main function
main()