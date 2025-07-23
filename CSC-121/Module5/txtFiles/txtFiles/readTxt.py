def main():
    # 3 step approach
    #1 create a file object (define the mode, if not read)
    #read, write or add are the 3 options 
    file = open('philosphers.txt','r') # it wil open in read mode

    #2 reading 
    #reading methods are read(), readline() and readlines()

    print(file.readline()) # it reads the 1st line

    while line !='':
            print(line.strip())

            line = file.readline()

    #3 
    #closes the file 
    file.close()

if __name__ =="__main__":
    main()

    #we dont need readline in a for lop
def main2():
    # 3 step approach
    #1 create a file object (define the mode, if not read)
    #read, write or add are the 3 options 
    file = open('philosphers.txt','r') # it wil open in read mode

    #2 reading 
    #reading methods are read(), readline() and readlines()

    print(file.readline()) # it reads the 1st line

    for line in file:
            
        print(line.rstrip())

    #3 
    #closes the file 
    file.close()

if __name__ =="__main__":
    main()

#for loop
def main3():
    # 3 step approach
    #1 create a file object (define the mode, if not read)
    #read, write or add are the 3 options 
    file = open('philosphers.txt','r') # it wil open in read mode

    #2 reading 
    #reading methods are read(), readline() and readlines()

    print(file.readline()) # it reads the 1st line

    for line in file:
        line2 = line.split(' ')
        print(line)

    #3 
    #closes the file 
    file.close()

if __name__ =="__main__":
    main()


#for loop
def main4():
    # 3 step approach
    #1 create a file object (define the mode, if not read)
    #read, write or add are the 3 options 
    file = open('philosphers.txt','r') # it wil open in read mode

    #2 reading 
    #reading methods are read(), readline() and readlines()

    file.readlines()#read the entire content of the file into an iterable object (into a list basically)
    


    #3 
    #closes the file 
    file.close()

if __name__ =="__main__":
    main()

