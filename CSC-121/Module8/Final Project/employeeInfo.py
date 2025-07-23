import csv

class Employee:
    def __init__(self, empId, first_name, last_name, age, department, salary):
        self._empId = empId
        self._first_name = first_name
        self._last_name = last_name
        self._age = age
        self._department = department
        self._salary = salary
        self._email = self.set_email(first_name, last_name)

    def set_email(self, first, last):
        self._email = f"{last.lower()}.{first.lower()}@abc_company.com"
        return self._email

    def __repr__(self):
        return (f"Employee ID: {self._empId}, Name: {self._first_name} {self._last_name}, "
                f"Age: {self._age}, Department: {self._department}, "
                f"Salary: ${self._salary:.2f}, Email: {self._email}")


def read_file():
    employees_list = []
    try:
        with open('employees.csv', 'r') as employees_file:
            reader = csv.reader(employees_file)
            next(reader)  # Skip header
            for row in reader:
                empId, first_name, last_name, age, department, salary = row
                employee = Employee(empId.strip(), first_name.strip(), last_name.strip(),
                                    int(age), department.strip(), float(salary))
                employees_list.append(employee)
    except FileNotFoundError:
        print("⚠️ Error: 'employees.csv' not found. Make sure it's in the same folder as this script.")
    return employees_list


def create_report(employees):
    # CSV Report
    with open('employee_report.csv', 'r', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['ID', 'First Name', 'Last Name', 'Email', 'Age', 'Department', 'Salary'])
        for emp in employees:
            writer.writerow([
                emp._empId,
                emp._first_name,
                emp._last_name,
                emp._email,
                emp._age,
                emp._department,
                emp._salary
            ])

    # TXT Report
    with open('emp_report_txt.txt', 'w') as txtfile:
        txtfile.write("EMPLOYEE REPORT\n")
        txtfile.write("=" * 90 + "\n")
        txtfile.write(f"{'ID':<10}{'First Name':<15}{'Last Name':<15}{'Email':<30}{'Age':<5}{'Dept':<15}{'Salary':<10}\n")
        txtfile.write("-" * 90 + "\n")
        for emp in employees:
            txtfile.write(f"{emp._empId:<10}{emp._first_name:<15}{emp._last_name:<15}"
                          f"{emp._email:<30}{emp._age:<5}{emp._department:<15}${emp._salary:<10.2f}\n")


def menu():
    employees = []
    choice = 0
    while choice != 7:
        print("\n-------------------------Menu-------------------------")
        print("1) Read Employee Info and Create Class Objects/Instances")
        print("2) Add a New Employee Record")
        print("3) Update Employee Information")
        print("4) Search for Employee by Last Name")
        print("5) Search for Employee by Id")
        print("6) Generate Report")
        print("7) Exit")
        print("-------------------------------------------------------")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if choice < 1 or choice > 7:
            print("Invalid choice! Please choose a number from the list of options.")
            continue

        if choice == 1:
            employees = read_file()
            for emp in employees:
                print(emp)

        elif choice == 2:
            employees = read_file()
            empId = input("Enter Employee ID: ")
            if any(emp._empId == empId for emp in employees):
                print("Employee already exists and can't be added.")
                continue
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            age = int(input("Enter Age: "))
            department = input("Enter Department: ")
            salary = float(input("Enter Salary: "))
            new_employee = Employee(empId, first_name, last_name, age, department, salary)
            employees.append(new_employee)
            print(f"Added new employee: {new_employee}")

        elif choice == 3:
            employees = read_file()
            empId = input("Enter Employee ID to update: ")
            employee = next((emp for emp in employees if emp._empId == empId), None)
            if employee is None:
                print("Employee does not exist.")
                continue
            print("-------Update Employee Information----------")
            print("1) Update Employee Last Name")
            print("2) Update Employee Age")
            print("3) Update Employee’s Department")
            print("4) Update Employee’s Salary")
            print("-----------------------------------------------------")
            try:
                update_choice = int(input("Enter choice for update: "))
            except ValueError:
                print("Invalid input.")
                continue

            if update_choice == 1:
                new_last_name = input("Enter new Last Name: ")
                employee._last_name = new_last_name
                employee.set_email(employee._first_name, new_last_name)

            elif update_choice == 2:
                new_age = int(input("Enter new Age: "))
                employee._age = new_age

            elif update_choice == 3:
                new_department = input("Enter new Department: ")
                employee._department = new_department

            elif update_choice == 4:
                new_salary = float(input("Enter new Salary: "))
                employee._salary = new_salary

            else:
                print("Invalid update option.")
                continue

            print(f"Updated employee: {employee}")

        elif choice == 4:
            employees = read_file()
            last_name = input("Enter employee's last name: ")
            found = False
            for emp in employees:
                if emp._last_name.lower() == last_name.lower():
                    print(emp)
                    found = True
            if not found:
                print("Employee does not exist.")

        elif choice == 5:
            employees = read_file()
            emp_id_to_search = input("Enter Employee ID: ")
            found = False
            for employee in employees:
                if employee._empId == emp_id_to_search:
                    print(employee)
                    found = True
                    break
            if not found:
                print("Employee does not exist.")

        elif choice == 6:
            employees = read_file()
            if employees:
                create_report(employees)
                print("Reports generated: 'employee_report.csv' and 'emp_report_txt.txt'")
            else:
                print("No employee data available to generate report.")

        elif choice == 7:
            print("Goodbye!")
            break

menu()