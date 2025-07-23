#value returning function that takes arguements 
import functions as fn

def main():
    print("Program asks for name and says hi")
    f, hours = fn.get_name()

    print("Hello", f)
    gross = fn.get_rate_gross(hours)

    print(gross)

if __name__ == "__main__":
    main()