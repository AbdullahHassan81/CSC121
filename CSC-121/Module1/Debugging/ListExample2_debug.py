


def main():
    
    

    #Creates empty lists
    numList=[]
    wordList = []


    print("This program allows user to create a list containing either numbers or string, it then evaluates content and eliminates duplicates")

    print("\nLet us start with the number list")

    number = int(input("\nHow many numbers do you want to add to list? "))


    for x in range(number):
        num=int(input(f"Enter element number {x+1} : "))# you could do f string or concatanation
        numList.append(num)


    print("\nNow we move on to list of words/string")

    number = int(input("\nHow many elements do you want to add to list? "))


    for x in range(number):
        word=input("Enter element number "+str(x+1 )+": ")
        wordList.append(word)
        # print the two lists

    # pass list to function

    dis_results(numList, wordList)

def dis_results(numList, wordList):
    print("Original Number list:", numList)
    print("\nList without duplicates:", unique(numList))
    print()

    print("Original Word list:", wordList)
    print("\nList without duplicates:", unique(wordList))
    print()

                
def unique(values):
    #iterate = loop
    #add a for loop 
    no_duplicates =[]
    
    for x in values: 
        
        if x not in no_duplicates:
            #add the element to new list
            no_duplicates.append(x)
            
    return no_duplicates

        
   

                             

main()
