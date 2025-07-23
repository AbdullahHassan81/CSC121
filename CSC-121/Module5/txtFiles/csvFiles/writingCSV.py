#writing CSV files
import csv 

salaries = [4000, 5000]
with open('writeCSV1.csv', 'w', newline='') as file_csv:

    file = csv.writer(file_csv) #writer deals with lists

    file2 = csv.DictWriter(file_csv) #deals with dictionaries
    

    #if wanting to write into ONE row, use writerow()
    file.writerow(["Salary", "Salary + 500"]) # must be passed as a list 
    
    for item in salaries: 
        file.writerow([item,item+500])