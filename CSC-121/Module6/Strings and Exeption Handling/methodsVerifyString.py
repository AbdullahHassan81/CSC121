password = ['password_2024', 'Password_2024', 'Pass']

def evaluate(password):
    #check if 8 char min
    size = 0
    if len(password)>= 8:

        size = 1
    #Capital letter and #'s
    cap_yes = 0
    dig_yes = 0
    for ch in password: 
        #check if character is capital
       
        if ch.isupper():
            cap_yes = 1
        if ch.isdigit():
            dig_yes = 1

        sym = ["-", "_", "&"]
        sym_yes = 0
        for symbol in sym:
            if symbol in password:
                sym_yes = 1

    if size==1 and cap_yes ==1 and dig_yes ==1 and sym_yes==1:
        return True
    else:
        return False
passwords = ['password_2024', 'Password_2024', 'Pass']

for password in passwords:
    result = evaluate(password)

    print(password, result)