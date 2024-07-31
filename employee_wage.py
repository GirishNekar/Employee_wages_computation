"""
@Author: Girish
@Date: 2024-07-27
@Last Modified by: Girish
@Last Modified time: 2024-07-31
@Title: monthly wagw calculation 
"""

import random

def welcome_message():
    
    
    """
    Description : Prints a welcome message for the Employee Wage Computation Program.
    
    Parmeter : None
    
    return : None
    
    """
    
    
    print("Welcome to Employee Wage Computation Program")



def check_attendance():
    
    
    """
    Description : Simulates checking employee attendance.
     
    Parameter :   None

    Returns:
        str: "Present" or "Absent"
        
    """
    
    return random.choice(["Present", "Absent"])



def calculate_daily_wage(hours_worked, wage_per_hour=20):
    
    
    """
    Calculates the daily wage of an employee based on hours worked.

    Parameters:
        hours_worked (int): The number of hours worked in a day.
        wage_per_hour (int, optional): The wage per hour. Defaults to 20.

    Returns:
        int: The calculated daily wage.
    """
    
    
    return hours_worked * wage_per_hour



def calculate_monthly_wage(working_days=20, daily_hours=8, wage_per_hour=20):
    
    
    """
    Calculates the total monthly wage for an employee.

    Parameters:
        working_days (int, optional): The number of working days in a month. Defaults to 20.
        daily_hours (int, optional): The number of hours worked per day. Defaults to 8.
        wage_per_hour (int, optional): The wage per hour. Defaults to 20.

    Returns:
        int: The calculated total monthly wage.
        
    """
    daily_wage = calculate_daily_wage(daily_hours, wage_per_hour)
    return daily_wage * working_days




def main():

    welcome_message()
    try:
        employees = [
            {"type": "full-time", "attendance": check_attendance()},
            {"type": "part-time", "attendance": check_attendance()},
            {"type": "full-time", "attendance": check_attendance()},
            {"type": "part-time", "attendance": check_attendance()}
        ]

        for i, employee in enumerate(employees, start=1):
            print(f"\nEmployee {i} is {employee['attendance']} and is a {employee['type']} employee.")
            
            if employee['attendance'] == "Present":
                if employee['type'] == "full-time":
                    daily_hours = 8
                else:
                    daily_hours = 4
                
                daily_wage = calculate_daily_wage(daily_hours)
                monthly_wage = calculate_monthly_wage(daily_hours=daily_hours)
                
                print(f"Daily Wage: ${daily_wage}")
                print(f"Monthly Wage: ${monthly_wage}")
            else:
                print("No wage, employee is absent")

    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()
