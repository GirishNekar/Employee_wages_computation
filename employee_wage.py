"""
@Author: Girish
@Date: 2024-07-27
@Last Modified by: Girish
@Last Modified time: 2024-07-31
@Title: Employee Check Attendence Program
"""



import random

def welcome_message():
    
    
    """
    
    Prints a welcome message for the Employee Wage Computation Program.

    Description:
        This function displays a welcome message to the user when the program starts.
        
    return : None
    
    """
    
    print("Welcome to Employee Wage Computation Program")



def check_attendance():
    
    
    """
    Simulates checking employee attendance.

    Description:
        This function randomly returns either "Present" or "Absent" to simulate employee attendance.
    
    Returns:
        str: "Present" or "Absent"
        
        
    """
    return random.choice(["Present", "Absent"])



def main():

    welcome_message()        
    attendance = check_attendance()
    print(f"Employee is {attendance}")



if __name__ == "__main__":
    main()

