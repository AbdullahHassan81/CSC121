#void functions parameter variables 

def main():
    print("Program asks for name and says hi\n")

    first = input("Please enter your first name: ")
    print("Hello", first)

    hours = float(input("Hours Worked: "))
    rate = float(input("Enter Pay Rate: "))

    #call function without passig payrate 
    get_gross(hours)
    #call function and pass payrate
    get_gross(hours, rate)

def get_gross(h, r=20):

    gross = h * r
    print(gross)

if __name__ == "__main__":
    main()
