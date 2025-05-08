

class Pet:

    def __init__(self, name, age, p_type):

        self.__name = name
        self.__age = age
        self.__p_type = p_type


    def __repr__(self):

        return "Pet Name: "+self.__name+\
    "\nPet Type: "+self.__p_type+"\nPet Age: "+self.__age
    
    # setters name, age
    
    def set_name(self,new_name):
        
        self.__name = new_name

    def set_age(self,new_age):
        
        self.__age = new_age
    
    # getters 
    
    def get_name(self):
        
        return self.__name

    def get_age(self):
        
        return self.__age

    def get_type(self):
        
        return self.__p_type
    
    

