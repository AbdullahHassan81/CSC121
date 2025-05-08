# -*- coding: utf-8 -*-

import random as ran
def main():

    # get dicts

    #assign values to variables on the left side 
    capital, country = create_dict()
    

    incorrect = 0
    correct = 0

    #give user a value different from 0 so it can run 
    user = 'y'
    while user!='0':

        number=ran.randint(1,21)
        right='n'
        while right=='n':
            print("what is the capital of ", country[number], " press 0 to quit")
            user=input()
            if user == capital[number]:
                right='y'
                print ('you are correct, congratulations!')
                correct +=1
            elif user =='0':
                right='y'
            else:
                right='n'
                print('you are wrong')
                
                incorrect +=1
    print('you got ', correct, " correct and got " , incorrect, "incorrect. Thanks for playing" )

    print()
    # now print countries and their capitals
    display(capital,country)


def create_dict():
    
    # numbers are keys 
    capital= {1:'Kabul',2:'Mexico City',3:'Beijing',4:'Cairo',5:'Paris',6:'Budapest',7:'Rome',
              8:'Tokyo',9:'Kuwait City',10:'Tripoli',11:'Amsterdam',12:'Warsaw',13:'Moscow',
              14:'Madrid',15:'Seoul',16:'Taipei',17:'london',18:'Beirut',
              19:'Ottawa',20:'Lima'}
    country= {1:'Afghanistan',2:'Mexico',3:'China',4:'Egypt',5:'France',6:'Hungary',7:'Italy',
              8:'Japan',9:'Kuwait',10:'Libya',11:'Netherlands',12:'Poland',13:'Russia',
              14:'Spain',15:'South Korea',16:'Taiwan',17:'United Kingdom',18:'Lebanon',
              19:'Canada',20:'Peru'}

    #should have also returned country 
    return capital, country 

def display(capital, country):

    print(f'{"Country":<20}{"Capital"}')
    print("-"*45)

    #len gives the elements in the dictionary 
    #add the plus 1 because there is no 0 number
    for i in range(len(capital)):
        print(f'{country[i+1]:<20}{capital[i+1]:<20}')


if __name__ == "__main__":

    main()
    
    


