"""
@Author: Girish
@Date: 2024-07-30
@Last Modified by: Girish
@Last Modified time: 2024-08-01
@Title: Generating wage of a Employee on a condition
"""

import random

def welcome_message():
    """
    Prints a welcome message for the Employee Wage Computation Program.
    """
    print("Welcome to Employee Wage Computation Program")

def check_attendance():
    """
    Simulates checking employee attendance.

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

def calculate_monthly_wage(hours_list, wage_per_hour=20):
    """
    Calculates the total monthly wage based on a list of hours worked over multiple days.

    Parameters:
        hours_list (list of int): A list containing hours worked each day.
        wage_per_hour (int, optional): The wage per hour. Defaults to 20.

    Returns:
        int: The calculated total monthly wage.
    """
    total_wage = 0
    
    for hours in hours_list:
        daily_wage = calculate_daily_wage(hours, wage_per_hour)
        total_wage += daily_wage

    return total_wage

def main():
    """
    Main entry point of the program.

    Description:
        Calls the `welcome_message` function to display the welcome message, then
        randomly determines attendance for four employees over the last 20 days,
        collects working hours only for present days, calculates, and prints the monthly
        wage for each employee.
    """
    welcome_message()
    
    try:
        # Initialize variables
        num_days = 20
        wage_per_hour_full_time = 20
        wage_per_hour_part_time = 20
        
        # Employee data
        employees = {
            "Employee 1": [],
            "Employee 2": [],
            "Employee 3": [],
            "Employee 4": []
        }
        
        # Determine attendance and collect working hours
        for employee in employees:
            print(f"\nDetermining attendance and collecting working hours for {employee}:")
            for day in range(1, num_days + 1):
                attendance = check_attendance()
                if attendance == "Present":
                    try:
                        hours = int(input(f"Day {day}: "))
                        if hours < 0:
                            print("Invalid input. Hours worked cannot be negative.")
                            continue
                    except ValueError:
                        print("Invalid input. Please enter an integer value for hours.")
                        continue
                    employees[employee].append(hours)
                else:
                    employees[employee].append(0)  # No hours worked if absent

        # Calculate and print monthly wages for each employee
        for employee, hours_list in employees.items():
            print(f"\nCalculating monthly wage for {employee}:")
            wage_per_hour = wage_per_hour_full_time if "1" in employee or "2" in employee else wage_per_hour_part_time
            monthly_wage = calculate_monthly_wage(hours_list, wage_per_hour)
            print(f"{employee} Monthly Wage: ${monthly_wage}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
