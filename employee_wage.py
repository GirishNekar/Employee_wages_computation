"""
@Author: Girish
@Date: 2024-08-1
@Last Modified by: Girish
@Last Modified time: 2024-08-01
@Title: Generating wage of a Employee on a condition
"""


import random

WAGE_PER_HOUR = 20
FULL_TIME_HOUR = 8
PART_TIME_HOUR = 4
WORKING_DAY = 20
TOTAL_WORKING_HOUR = 100

def display_welcome_message():
    
    
    """
    Description:
        Prints the welcome message.

    Parameters:
        None

    Returns:
        None
    """
    
    
    print("Hello Everyone, welcome to Employee Wage Computation")



def get_employee_type():
    
    
    """
    Description:
        Returns whether the employee is working part-time or full-time.

    Parameters:
        None

    Returns:
        str: "Part_time" or "Full_time"
    """
    
    
    return random.choice(["Part_time", "Full_time"])

def get_attendance():
    
    
    """
    Description:
        Determines if the employee is present or absent.

    Parameters:
        None

    Returns:
        str: "Present" if present, "Absent" if absent
    """
    
    
    return random.choice(["Present", "Absent"])



def employee_daily_wage(wage_per_hour, work_hour):
    
    
    """
    Description:
        Calculates the employee's daily wage.

    Parameters:
        wage_per_hour (int): Employee's wage per hour
        work_hour (int): Employee's working hours

    Returns:
        int: Daily wage
    """
    
    
    return work_hour * wage_per_hour



def main():
    
    try:
        display_welcome_message()
        print("Employee Wage for the month:")

        work_day = 1
        work_hour = 0
        wage_list = []
        total_wage = 0

        while work_hour <= TOTAL_WORKING_HOUR and work_day <= WORKING_DAY:
            attendance = get_attendance()
            if attendance == "Present":
                employee_type = get_employee_type()
                if employee_type == "Full_time":
                    daily_work_hours = FULL_TIME_HOUR
                else:
                    daily_work_hours = PART_TIME_HOUR

                work_hour += daily_work_hours
                daily_wage = employee_daily_wage(WAGE_PER_HOUR, daily_work_hours)
                wage_list.append(daily_wage)
                total_wage += daily_wage
            else:
                wage_list.append(0)

            work_day += 1

        print("Wage list of Employee :")
        print(wage_list)
        print(f"Total wage: ${total_wage}")



    except Exception as e:
        print(e)



if __name__ == "__main__":
    main()

