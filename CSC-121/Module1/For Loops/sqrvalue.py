#calculating sqr value 
#for loop for a range of numbers
start = int(input("Starting Number: "))
end = int(input("Ending Number: "))
print(f'{"Num":<7}{"Sqr"}')
#get the # from the range
#the range function can pass up to 3 values
#this is hard coded
for num in range(5,15,):

    #calculate the sqr value
    sqr = num**2

    #display the num and sqr 
    print(num, sqr)


#this is not hard coded
print(f'{"Num":<7}{"Sqr"}')
print("-" *30)
#get the # from the range
#the range function can pass up to 3 values
#this is hard coded


for num in range(start,end+1):

    #calculate the sqr value
    sqr = num**2
    #display the num and sqr 
    print(f'{num:<7}{sqr}')
