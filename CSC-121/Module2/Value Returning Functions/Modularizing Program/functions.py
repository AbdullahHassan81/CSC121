#modularizing functions
def main():
    print("testing")
def get_name():
    first = input("Please enter your first name: ")
    hours = float(input("Hours Worked: "))

    return first, hours 

def get_rate_gross(h):
    gross = h * 25
    return gross

if __name__ == "__main__":
    main()