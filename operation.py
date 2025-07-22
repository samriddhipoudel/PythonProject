import read  # Importing read.py module
import write  # Importing write.py module
from datetime import date

def display_lands(data_dictionary): # helper method to display land info
    print("\n" + "_" * 84)
    print(f"{'S.N.':<4} | {'kiita':<6} | {'location':<10} | {'Direction':<10} | {'Annas':<5} | {'Cost':<7} | {'Availability':<12}")
    print("_" * 84)
    read.file_write()
    print("_" * 84 + "\n")

def for_rent():
    """
    This is the function to handle the renting process, it collects customer details,
    the land they want to rent, Updates availability the availability of land according to the user choice
    and generates a rental bill.
    """
    items_bought = []  # Initializing an empty list to store rented items
    data_dictionary = read.read_data()  # Read land data from file

    print("\n" + "_" * 84)
    while True:
        customer_name = input("Enter your Name: ")
        if customer_name.isdigit():
            print("Please enter a valid name.")
        else:
            break

    while True:
        print("\n" + "_" * 84)
        try:
            customer_number = int(input("Enter your Number: "))
            break
        except ValueError:
            print("Enter a valid number")

    while True:
        display_lands(data_dictionary) 

        try:
            chosen_symbol = int(input("Enter the symbol number that you wish to purchase: "))
            if data_dictionary[chosen_symbol][5].strip() == "Available":
                data_dictionary[chosen_symbol][5] = "Not Available"

                while True:
                    try:
                        duration_rent = int(input("Enter for how long you would like to rent this place, in months: "))
                        break
                    except ValueError:
                        print("Enter a valid number")

                write.write_data(data_dictionary)  # Update land availability in file 
                items_bought.append(data_dictionary[chosen_symbol])  # Add rented land to list

                response = input("Would you like to continue further?: ").lower()
                if response == 'n':
                    break 
                elif response != 'y':
                    print("Printing bill...")
                    break 
            else:
                print("The land is not available")
        except (KeyError, ValueError):
            print("Invalid input")

    if items_bought:
        write.to_generate_bill(customer_name, customer_number, items_bought, duration_rent)  # Generating the bill for renting land

def for_return_land():
    """
    This is a function to handle the land return process, it collects customer details and
    the land they want to return. It also Updates availability according to the returnes land, calculates fine (if any),
    and generates a return bill.
    """
    items_returned = []  # Initializing a list to store returned items
    fine = 0  # Initializing the fine amount
    data_dictionary = read.read_data()  # Read land data from the file

    print("\n" + "_" * 84)
    while True:
        customer_name = input("Enter your Name: ")
        if customer_name.isdigit():
            print("Please enter a valid name .")
        else:
            break

    while True:
        print("\n" + "_" * 84)
        try:
            customer_number = int(input("Enter your Number: "))
            break
        except ValueError:
            print("Enter a valid number")

    while True:
        display_lands(data_dictionary) 

        try:
            chosen_symbol = int(input("Enter the symbol number that you wish to return: "))
            if data_dictionary[chosen_symbol][5].strip() == "Not Available":
                data_dictionary[chosen_symbol][5] = "Available"

                while True:
                    try:
                        duration_rent = int(input("Enter the time period you rented this place for (in months): "))
                        break
                    except ValueError:
                        print("Enter a valid number")

                while True:
                    try:
                        return_time = int(input("Enter the return time: "))
                        break
                    except ValueError:
                        print("Enter a valid number")

                if duration_rent < return_time:
                    fine = 0.1 * int(data_dictionary[chosen_symbol][4]) * (return_time - duration_rent)

                write.write_data(data_dictionary)  # Update land availability in file
                items_returned.append(data_dictionary[chosen_symbol])  # Adding the returned returned land to list

                response = input("Would you like to continue further? (y/n): ").lower()
                if response == 'n':
                    break 
                elif response != 'y':
                    print("Printing the bill...")
                    break 
            else:
                print("The land is not rented")
        except (KeyError, ValueError):
            print("Invalid input")

    if items_returned:
        write.generate_bill_return(customer_name, customer_number, items_returned, return_time, fine)  # Generating the bill for returned lands
