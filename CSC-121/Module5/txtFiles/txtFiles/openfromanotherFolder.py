def main():
    #raw path 
    #this is how to open a txt file from another folder
    with open(r'D:\Semester2\CSC-121\Module5\txtFiles\New folder\philosphers.txt') as file:

        for line in file:
            print(line)

if __name__ == "__main__":
    main()