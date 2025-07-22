def read_data():
    try:
        dictionary_data = {}  # Initialize an empty dictionary to store data
        with open("land.txt", "r") as file_obj:  # Open the file "land.txt" to read
            id_number = 1  # Initialize an ID number starting from 1
            for line in file_obj:  
                line = line.strip()  # Remove whitespace and newline characters
                dictionary_data[id_number] = line.split(',')  # Split the line into a list using ',' and store it in dictionary
                id_number += 1  # Increment ID number for next entry
        return dictionary_data  # Return the dictionary containing read data
    except Exception as e:
        print("Error:", e)  # Print any errors found during file operation
        return None  # Return None if an error occurs

def file_write():
    try:
        with open("land.txt", 'r') as file_obj:  # For opening the file "land.txt" for reading
            serial_number = 1  # Initialize a serial number starting from 1
            for line in file_obj:  # Iterates through each line in the file
                fields = line.strip().split(',')
                print(f"{serial_number:<4} | {fields[0].strip():<6} | {fields[1].strip():<10} | {fields[2].strip():<10} | {fields[3].strip():<5} | {fields[4].strip():<7} | {fields[5].strip():<12}")  # Print the serial number and fields with proper alignment
                serial_number += 1  # Increasing serial number for next li
    except Exception as e:
        print("Error:", e)  # Print errors found 
