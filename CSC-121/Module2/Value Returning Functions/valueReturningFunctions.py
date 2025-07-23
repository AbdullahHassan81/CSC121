"""
value returning functions 
have to return a value(work like a void function)
could be created to take or not take arguements
could assign parameter var (if defined) default values
"""
def main():
    print("Program asks for name and says hi")
    f, l = get_name()

    print("Hello", f)

def get_name():
    """
    this function gets first and last name
    """

    first = input("Please enter your first name: ")
    last = input("Please enter your last name: ")

    return first, last

if __name__ == "__main__":
    main()
