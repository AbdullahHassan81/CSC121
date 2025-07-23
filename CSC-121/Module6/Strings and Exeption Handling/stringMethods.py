#string basics and slicing

with open('name_list.txt') as inflie, open('report.txt', 'w') as outFile:

    #using f string
    #outFile.wirte(f'{"Student Report":^100}\n')
    outFile.wirte(f'{"Student Report".center(100)}\n')
    outFile.write("FirstName".ljust(15)+"LastName".ljust(15)+"Stu ID".ljust(10)+\
                  "Login".ljust(15)+"Email\n")
    for line in infile: 

        first = line[:9].rstrip()

        last = line[11:22].rstrip()

        stuID = line[-7:].rstrip()

        username = last[:7].lower()+first[0].lower()+stuID[-5]
        print(username)

        email = username + '@student.faytechcc.edu'

        #write to file
        outFile.write("FirstName".ljust(15)+"LastName".ljust(15)+"Stu ID".ljust(10)+\
                  "Login".ljust(15)+"Email\n")