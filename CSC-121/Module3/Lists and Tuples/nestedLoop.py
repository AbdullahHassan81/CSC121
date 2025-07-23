#nested lists
names = ['Muhammad', 'Aser', 'Ahmed', 'Omar' ]

#scenario 1 need to print out content 
print("\nScen 1")
for name in names:
    print(name)

#scenario2 need to print out indexes
print("\n Scen 2")
for i in range(len(names)): #range only takes numbers(int)
    print(i)

#scenario 3 need to print out indexes and content 
print("\nScen 3")
for i in range(len(names)): #range only takes numbers(int)
    print(i, names[i])
#OR
print("\nScen 3 Option2")
for i, name in enumerate(names): # range only takes numbers(int)
    print(i, name)

#print content of nested list
#1st list has names 2nd list has scores
stu_scores = [['Muhammad', 'Aser', 'Ahmed', 'Omar'], [98, 85, 99, 100]]

print("\nScen 4 Nested List")
for row in stu_scores:
    for col in row: #inner loop prints content for each row 
        print(col, end="\t")
        print() #this sperates the rows 