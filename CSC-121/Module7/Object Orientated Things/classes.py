 #the underscores protects attirbutes (2 underscores)
#the user can change the attribute if its not protected

# Define a class called Pet to represent a pet's information
class Pet:
    # Constructor to initialize the Pet instance with name, age, and type
    def __init__(self, name, age, p_type):
        self.__name = name             # Private attribute for pet's name
        self.__animal_type = p_type    # Private attribute for pet's type (Dog, Cat, etc.)
        self.__age = age                # Private attribute for pet's age

    # String representation method to return a readable format of Pet information
    def __repr__(self):
        return "Name: " + self.__name + "\nAge: " + str(self.__age) + "\nType: " + self.__animal_type

    # Mutator (setter) method to change the name of the pet
    def set_name(self, new):
        self.__name = new  # Update the private name attribute to the new value 

    # Mutator (setter) method to change the age of the pet
    def set_age(self, age):
        self.__age = age  # Update the private age attribute to the new value

    # Accessor (getter) method to retrieve the name of the pet
    def get_name(self):
        return self.__name  # Return the private name attribute

    # Accessor (getter) method to retrieve the age of the pet
    def get_age(self):
        return self.__age  # Return the private age attribute 

# Create a Pet object named pet1 with specific name, age, and type
pet1 = Pet("Smokke", 3, "Dog")

# Print statement to display information before changing the name
print("\nBefore")
print(pet1)  # Calls __repr__ to display Pet information

# Change the pet's name using the set_name method
pet1.set_name("Smoke")

# Print statement to indicate the change and show the updated name
print("\nAfter")
print(pet1.get_name())  # Get and print the updated name of the pet