from datetime import date

def write_data(dictionary_data):
    try:
        with open("land.txt", "w") as file_obj:  # Open the file "land.txt" for writing
            for values in dictionary_data.values():  # Iterate through each value in the dictionary
                file_obj.write(','.join(map(str, values)) + "\n")  # Convert the values to string and join with ',' to write to the file
    except Exception as e:
        print("Error writing to file:", e)  # Print error message if writing fails

def to_generate_bill(name, number, items, duration):
    try:
        # Calculate total cost based on items and duration
        total_cost = sum(int(item[4]) * duration for item in items)
        bill_heading_rent()  # Print heading for rent bill
        for_customer_details(name, number)  # Print customer details
        for_rental_items(items)  # Print rental items
        for_total_cost(total_cost)  # Print total cost
        write_to_file(name, number, "Rent", items, total_cost)  # Write bill details to file
    except Exception as e:
        print("Error generating rent bill:", e)  # Print error message if bill generation fails

def generate_bill_return(name, number, items, return_time, fine):          # Calculate total cost including fine based on items and return time
    try:
        # Calculate total 
        total_cost = sum(int(item[4]) * return_time for item in items)
        fine = total_cost * 0.10
        bill_heading_return()  # Print heading for return bill
        for_customer_details(name, number)  # Print customer details
        for_rental_items(items)  # Print rental items
        for_fine_and_total_cost(fine, total_cost)  # Print fine and total cost
        write_to_file(name, number, "Return", items, total_cost + fine)  # Write return bill details to file
    except Exception as e:
        print("Error generating return bill:", e)  # Print error message if return bill generation fails

def bill_heading_rent():    # Print heading for rent bill
    
    print("\n\n\n")
    print("\n" + "_" * 84 +"\n" )
    print("\n\n\t\t\tTechno Property Nepal Renting Bill\n\n\n")
    print("\n\tPhone Number: 9849289838\t\tAddress: Anamnagar")
    print("\n" + "_" * 84 +"\n" )

def bill_heading_return():  # Print heading for return bill
    
    print("\n\n\n")
    print("_" * 84  )
    print("\n\n\t\t\tTechno Property Nepal Return Bill")
    print("\n\tPhone Number: 9849289838\t\tAddress: Anamnagar")
    print("_" * 84  )

def for_customer_details(name, number):    # Print customer details
    
    print("\n\nName:", name, "\t\t\t\tContact Number:", number)
    print("_" * 84 )

def for_rental_items(items):   # Print the details
    
    print("_" * 84 )
    print("S.N.\t|Kitta\t|Location\t|Direction\t|Annas\t|Rental Cost")
    print("\n" + "_" * 84 +"\n" )
    serial_number = 1
    for item in items:
        # Print each item with serial number, kitta, location, direction, annas, and rental cost 
        print(f"{serial_number}|\t|{item[0]}\t|{item[1]}\t|{item[2]}\t\t|{item[3]}\t|{item[4]}")
        print ("\n" + "_" * 84 +"\n" )
        serial_number += 1

def for_total_cost(total_cost):
    # Print total cost for rent bill
    print("\n\n\n")
    print("_" * 84 )
    print("Total Cost:", total_cost, "\t\t\t\tRental Date:", date.today())
    print("_" * 84 +"\n\n\n\n\n\n\n\n\n\n")

def for_fine_and_total_cost(fine, total_cost):
    # Print fine, total cost, and return date for the return bill
    print("\n\n\n")
    print( "_" * 84 )
    print("Fine:", fine, "\t\t\t\tTotal Cost:", total_cost)
    print("Grand Total:", total_cost + fine, "\t\t\t\tReturn Time:", date.today())
    print("\n" + "_" * 84 +"\n\n\n\n\n\n\n\n\n\n")

def write_to_file(name, number, bill_type, items, total_amount):
    try:
        filename = f"invoice{name}_{bill_type}.txt"  # Generate filename based on customer name, number, and bill type
        with open(filename, "w") as file_obj:  # Open the file for writing
            # Write bill details to file
            file_obj.write(f"\n\n\n\t\t\tTechno Property Nepal {bill_type} Bill\n\n")
            file_obj.write("\n\n\n\n\tPhone Number: 9849289838\t\tAddress: Anamnagar")
            file_obj.write("\n" + "_" * 84 +"\n" )
            file_obj.write(f"\n\nName:{name}\t\t\t\tContact Number:{number}")
            file_obj.write("\n" + "_" * 84 +"\n" )
            file_obj.write("S.N.\t|Kitta\t|Location\t|Direction\t|Annas\t|Rental Cost\n")
            file_obj.write("\n" + "_" * 84 +"\n" )
            serial_number = 1
            for item in items:
                # Write each item with serial number, kitta, location, direction, annas, and rental cost to file
                file_obj.write(f"{serial_number}|\t|{item[0]}\t|{item[1]}\t|{item[2]}\t\t|{item[3]}\t|{item[4]}\n")
                serial_number += 1
            file_obj.write("\n\n\n")
            file_obj.write("\n" + "_" * 84 +"\n" )
            file_obj.write(f"Total Amount:{total_amount}\t\t\t\t{bill_type} Date:{date.today()}")
            file_obj.write("\n" + "_" * 84 +"\n\n\n\n\n\n\n\n\n\n")
    except Exception as e:
        print("Error writing to file:", e)  # Print error message if writing to file fails
