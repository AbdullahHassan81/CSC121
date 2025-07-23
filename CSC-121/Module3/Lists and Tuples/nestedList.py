#displaying a bar chart 
numbers = [19, 3, 15, 7, 11]

print('\nCreating a bar chart from numbers:')
print(f'Index{"Value":>8}    Bar')

#enumerate returns the index position and the value 
for index, value in enumerate(numbers):
    print(f'{index:>5}{value:>8}       {"*" * value}')