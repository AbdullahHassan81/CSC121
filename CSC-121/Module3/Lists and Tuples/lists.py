"""
lists are 0 indexed meaning it starts off with a zero
items or elements can be different data types
Allows duplicates and can be changed(Mutable)
Go to Jupyter 01_slicing, w3schools and jupyter 02_list methods 
Jupyter 03_searching, 06_passing to funcitons
"""
numbers = [10, 3, 7, 1, 9]
def modify(items):
    for x in items:
        print(x, x*2)

def modify_elements(items):
    """
    Mutliplies all the elements by 2 
    """
    for i in range(len(items)):
        items[1] *= 2
        #another way to write it would be 
        #print(i, items[i]*2)

modify(numbers)
