#void functions that require arguements 
#the first void one does not require arguements 

def main():
    """
    gets the first and last name
    calls the get name function 
    """

    print("Program will get your name and says hi\n")

    first = input("Enter First Name: ") #need to pass this value
    last = input("Enter Last Name: ")
    get_name(first, last)

def get_name(f, l):
    """
    says hi to first and last name
    """
    print("Hello", f, l)

if __name__ == "__main__":
    main()

