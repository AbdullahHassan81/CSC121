#void functions
'''
Dosent return a value
could be created to not take/take arguements
could assign parameter var (if defined) default values

'''
def main():
    print("Program asks for name and then says hi\n")
    get_name()

def get_name():
    """
    Function asks for name
    """
    name = input("Enter your name: ")
    print("Hello", name)

if __name__ == "__main__":
    main()