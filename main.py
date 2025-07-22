import datetime
import read
import operation
from datetime import date

current_date = date.today()
recent_date= current_date.strftime("%b %d, %Y\t\t\t\t\t\t\t\t%A") #formatting the current date along with the day 

def welcome_message():
    print( "_" * 84 +"\n")
    print(recent_date)
    print("\n\n\t\t\tWelcome to TechnoPropertyNepal\n")

    print("\n\tPhone Number: 9849289838\t\t\tAddress: Anamnagar")
    print( "_" * 84)
    print("\n\t\t\tChoose one option to continue")
    print("_" * 84)
    print(" \tto rent land\t\t\t| \t\tselect 1 ")
    print( "_" * 84+ "\n")
    print(" \tto return land\t\t\t| \t\tselect 2 ")
    print( "_" * 84+ "\n")
    print(" \tto exit program\t\t\t| \t\tselect 3 ")
    print( "_" * 84 +"\n\n" )

def to_exit_system():
    print("Thank you for using this system")

def for_user_choice():
    try:
        user_choice = input("Enter your selection: ")
        if user_choice == "1":
            operation.for_rent()
        elif user_choice == "2":
            operation.for_return_land()
        elif user_choice == "3":
            to_exit_system()
            return False  # Exit the loop
        else:
            print("Invalid input\n\n\n\n\n\n\n")
    except Exception as e:
        print("An error occurred:", e)
    return True  # Continue the loop

def main():
    try:
        while True:
            welcome_message()
            if not for_user_choice():
                break  # Exit the loop if handle_user_choice returns False
    except KeyboardInterrupt:
        print("\nThe user terminated the program.")

if __name__ == "__main__":
    main()

