#basically m5pro but with CSV instead of txt 
#7/13/25
#Abdullah Hassan

def menu():
    print("-----------------------Menu-----------------------")
    print("1) Search by Team (list number of times team won)")
    print("2) Search by Year")
    print("3) Get file Listing Number of Times Each Time Won")
    print("4) Exit")
    print("--------------------------------------------------")

choice = 0  
while choice != 4:  # Change to 4 since the menu has 4 options
    menu()
    choice = int(input("Enter choice: "))

    if choice == 1:
        try:
            with open('WorldSeriesWinners.csv', 'r') as file:
                content = file.readlines()  
                team_name = input("Enter the name of the team: ").strip()  # User enters team name
                team_name_found = False  # Flag to check if the team was found
                years = []  # List to store winning years
                
                for line in content:
                    if team_name in line:  # Check for direct match
                        year = line.split()[0]  # Extract the year from the line
                        years.append(year)  # Add winning year to the list
                        team_name_found = True  # Mark that the team was found
                
                if team_name_found:
                    # Format and display the wins and years
                    num_wins = len(years)  # Count number of wins
                    years_formatted = ', '.join(years)  # Join years for display
                    print(f"The team '{team_name}' won {num_wins} time(s) in the following year(s): {years_formatted}")
                else:
                    print(f"The team '{team_name}' was not found in the file.")
        except FileNotFoundError:
            print("File 'WorldSeriesWinners.csv' not found.")

    elif choice ==2:
        try:
            with open('WorldSeriesWinners.csv', 'r') as file:
                content = file.readlines()  # Read content here, not from choice 2
                # Initialize year variable
                year = input("Enter the year (1990-2022): ")
                
                # Validate the year
                if year.isdigit() and 1990 <= int(year) <= 2022:
                    found = False
                    
                    for line in content:
                        if line.startswith(year):  # Check if the line starts with the entered year
                            team = line.split()[1]  # Assuming the second word is the team name
                            print(f"The team that won in {year} is: {team}")
                            found = True
                            break
                    
                    if not found:
                        print(f"No team found for the year {year}.")
                else:
                    print("Invalid year. Please enter a year between 1990 and 2022.")
        except FileNotFoundError:
            print("File 'WorldSeriesWinners.csv' not found.") 

    elif choice ==3: 
        try:
            with open('WorldSeriesWinners.csv', 'r') as file:
                content = file.readlines()  # Read content here
                
                # Create a dictionary to count wins per team
                team_wins = {}
                
                for line in content:
                    if line.strip():  # Skip empty lines
                        parts = line.split()
                        if len(parts) >= 2:  # Ensure line has at least 2 parts
                            team = parts[1]
                            if team in team_wins:
                                team_wins[team] += 1
                            else:
                                team_wins[team] = 1
                
                # Create the TXT file
                with open('Winners.txt', 'w') as txt_file:
                    txt_file.write("Team\tWins\n")  # Write title
                    for team, wins in team_wins.items():
                        txt_file.write(f"{team}\t{wins}\n")
                
                # Create the CSV file
                with open('Winners.csv', 'w') as csv_file:
                    csv_file.write("Team,Wins\n")  # Write title
                    for team, wins in team_wins.items():
                        csv_file.write(f"{team},{wins}\n")
                
                print("Files 'Winners.txt' and 'Winners.csv' have been created successfully.")
        except FileNotFoundError:
            print("File 'WorldSeriesWinners.csv' not found.")
    

    elif choice ==4: 
        print("Goodbye!")

print("Program ended.")
