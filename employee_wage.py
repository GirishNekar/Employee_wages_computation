"""
@Author: Girish
@Date: 2024-07-27
@Last Modified by: Girish
@Last Modified time: 2024-07-31
@Title: Part time and full time employee wages

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



def calculate_daily_wage(hours_worked, wage_per_hour=20):
    
    
    """
    Calculates the daily wage of an employee based on hours worked.

    Description:
        This function computes the daily wage by multiplying the number of hours worked
        by the wage per hour.

    Parameters:
        hours_worked (int): The number of hours worked in a day.
        wage_per_hour (int, optional): The wage per hour. Defaults to 20.

    Returns:
        int: The calculated daily wage.
        
    """
    
    return hours_worked * wage_per_hour

def main():

    welcome_message()
    
    try:
        
        attendance_full_time = check_attendance()
        print(f"Employee is {attendance_full_time}")

        attendance_part_time = check_attendance()
        print(f"Employee is {attendance_part_time}")
        
        FULL_DAY_HOURS = 8
        PART_DAY_HOURS = 4
        
        if attendance_full_time == "Present":
            daily_wage = calculate_daily_wage(FULL_DAY_HOURS)
            print(f"Daily Wage: ${daily_wage}")
        else:
            print("No wage, employee is absent")



        if attendance_part_time == "Present":
            daily_wage = calculate_daily_wage(PART_DAY_HOURS)
            print(f"Daily Wage: ${daily_wage}")
        else:
            print("No wage, employee is absent")
        
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()
