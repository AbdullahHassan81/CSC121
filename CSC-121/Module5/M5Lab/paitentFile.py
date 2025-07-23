#txt file
#used python tutor


import csv  # Needed for working with CSV files

# Initialize the program
keep_going = "y"
while keep_going == "y":
    patient_id = input("Patient ID: ")  # Corrected typos in patient
    height = float(input("Patient Height (in inches): "))  # Added prompt clarity
    weight = float(input("Patient Weight (in pounds): "))  # Added prompt clarity
    
    # Calculate BMI
    bmi = weight / height ** 2 * 703
    print(f"BMI: {bmi}")  # Show calculated BMI
    print(f"Patient ID: {patient_id}, Height: {height}, Weight: {weight}")
    
    # Save patient data to a CSV file
    with open('patient_bmi.csv', 'a', newline='') as csv_file:  # Open CSV file in append mode
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([patient_id, height, weight, bmi])  # Save as a row in CSV format

    keep_going = input("Do you have another patient? (y for yes): ")

# New functionality to read the data from patient_bmi.csv and display it
try:
    with open('patient_bmi.csv', 'r') as csv_file:  # Changed from bmi.txt to patient_bmi.csv
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            pid = row[0]
            h = row[1]
            w = row[2]
            if h.replace('.', '', 1).isdigit() and w.replace('.', '', 1).isdigit():  # Check if height and weight are numeric
                bmi = float(w) / float(h) ** 2 * 703  # Calculate BMI
                print(f"Patient ID: {pid}, BMI: {bmi}")
            else:
                print(f"Error: Non-numeric data for Patient ID: {pid}")  # Display error
except FileNotFoundError:
    print("No records found, please add a patient first.")


'''
# Initialize the program
keep_going = "y"
while keep_going == "y":
    patient_id = input("Patient ID: ")  # Corrected typos in patient
    height = float(input("Patient Height (in inches): "))  # Added prompt clarity
    weight = float(input("Patient Weight (in pounds): "))  # Added prompt clarity
    
    # Calculate BMI
    bmi = weight / height ** 2 * 703
    print(f"BMI: {bmi}")  # Show calculated BMI
    print(f"Patient ID: {patient_id}, Height: {height}, Weight: {weight}")
    
    # Save patient data to the file
    with open('bmi.txt', 'a') as bmi_file:  # Changed 'w' to 'a' to append data
        bmi_file.write(f'{patient_id},{height},{weight},{bmi}\n')  # Save to CSV format

    keep_going = input("Do you have another patient? (y for yes): ")

# New functionality to read the data from bmi.txt and display it
try:
    with open('bmi.txt', 'r') as bmi_file:
        for line in bmi_file:
            data = line.strip().split(',')
            pid = data[0]
            h = data[1]
            w = data[2]
            if h.isnumeric() and w.isnumeric():  # Check if height and weight are numeric
                bmi = float(w) / float(h) ** 2 * 703  # Calculate BMI
                print(f"Patient ID: {pid}, BMI: {bmi}")
            else:
                print(f"Error: Non-numeric data for Patient ID: {pid}")  # Display error
except FileNotFoundError:
    print("No records found, please add a patient first.")
'''
