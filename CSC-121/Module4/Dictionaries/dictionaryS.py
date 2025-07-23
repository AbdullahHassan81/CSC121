#dict
names_dict = {123: 'Chris',234: 'Sussie', 456:'Jessica', 365:'Simon'}

for k, v in names_dict():
    print(k, v)

#or you could do 
# k = names_dict.keys()
# print(k)
# v = names_dict.values()
# print(v)
#it will print both keys and values 
#keys are 1234 and values are the names
# to split the keys and values 
# do for k, v in names_dict.items():
#   print(k,v)
# and use display using a tabular format 
# print(f'{"Stu ID":<10}{"Name"}') 