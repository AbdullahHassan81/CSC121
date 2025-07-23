contacts = {}

print('Enter email and phone # at > prompt (<return> when done)')
entry = input('> ')
while entry != '':
    email, phone = entry.split()
    contacts[email] = phone # add entry to dictionary
    print(contacts)
    entry = input('> ') #if we dont have this line than an infinite loop will be made 
    #find dictionary methods on w3Schools