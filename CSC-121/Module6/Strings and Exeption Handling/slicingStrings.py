#string basics and slicing

with open('name_list.txt') as inflie:

    for line in infile: 

        first = line[:9].rstrip()

        last = line[11:22].rstrip()

        stuID = line[-7:].rstrip()

        username = last[:7]+first[0]+stuID[-5]
        print(username)

        email = username + '@student.faytechcc.edu'

        #write to file

        #using f string
        outFile.wirte(f'{"Student Report":^100}\n')
        outFile.write('Student Report\n'.center(100)+'\n')