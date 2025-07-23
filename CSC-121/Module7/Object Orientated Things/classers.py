class Pet:
    def __init__(self, name, age, p_type):
        self.__name = name
        self.__animal_type = p_type
        self.__age = age
    
    #def __repr__(self):

    #return "Name: "+self.__name+"\nAge: "+str(self.__age)+"\nType: "+self.__animal_type

pet1 = Pet("Smoke", 3, "Dog")
print(pet1)