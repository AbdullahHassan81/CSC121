names = {123:'Chris', 456:'Sussie', 789:'Jessica', 963:'Simon'}

print("\nScen 1")

#print keys 
for name in names:
    print(name)

#print values 
print("\nScen 2")

for name in names.values():
    print(name)

#print both keys and values
print("\nScen 3")

for stu_id, name in names.items():

    print(stu_id, name)

#differet dict, one that has a nested dict 
grades = {'Chris': {"Math":87, "Sci":99}, 'Sussie':{"Math":77, "Sci":70}, 'Jessica':{"Math":100, "Sci":89}, 'Simon':{"Math":93, "Sci":87}}
#get the name and scores for each student and display on the same line
print("\nScen 4")

print(f'{"Name":<15}{"Math":<10}{"Science"}')
for name, scores in grades.items():
    print(f'{name:<15}', end='')
    #iterate over nested dict
    for quiz_name, score in scores.items():
        print(f'{scores:<10}')
        print()


print(f'{"Name":<15}{"Math":<10}{"Science"}')
for name, scores in grades.items():
    print(f'{name:<15}{scores["Math"]:<10}{scores["Sci"]}')