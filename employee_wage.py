"""
@Author: Girish
@Date: 2024-08-01
@Last Modified by: Girish
@Last Modified time: 2024-08-01
@Title: Generating wage of an Employee on a condition using class methods
"""


import random

class Employee:
    WAGE_PER_HOUR = 20
    FULL_TIME_HOUR = 8
    PART_TIME_HOUR = 4
    WORKING_DAY = 20
    TOTAL_WORKING_HOUR = 100

    @classmethod
    def display_welcome_message(cls):
        
        
        """
        Description:
            Prints the welcome message.

        Parameters:
            cls : Used for accessing the class level data 

        Returns:
            None
        """
        
        
        print("Hello Everyone, welcome to Employee Wage Computation")



    @classmethod
    def get_employee_type(cls):
        
        
        """
        Description:
            Returns whether the employee is working part-time or full-time.

        Parameters:
            cls : Used for accessing the class level data 

        Returns:
            str: "Part_time" or "Full_time"
        """
        
        
        return random.choice(["Part_time", "Full_time"])

    @classmethod
    def get_attendance(cls):
        
        
        """
        Description:
            Determines if the employee is present or absent.

        Parameters:
           cls : Used for accessing the class level data 

        Returns:
            str: "Present" if present, "Absent" if absent
        """
        
        
        return random.choice(["Present", "Absent"])

    @classmethod
    def employee_daily_wage(cls, work_hour):
        
        
        """
        Description:
            Calculates the employee's daily wage.

        Parameters:
            work_hour (int): Employee's working hours
            cls : Used for accessing the class level data 

        Returns:
            int: Daily wage
        """
        
        
        return work_hour * cls.WAGE_PER_HOUR

    @classmethod
    def compute_monthly_wage(cls):
        
        
        """
        Description:
            Computes the total wage for the employee for the month.

        Parameters:
           cls : Used for accessing the class level data 

        Returns:
            int: Total wage for the month
        """
        
        
        cls.display_welcome_message()
        print("Employee Wage for the month:")

        work_day = 1
        work_hour = 0
        wage_list = []
        total_wage = 0

        while work_hour <= cls.TOTAL_WORKING_HOUR and work_day <= cls.WORKING_DAY:
            attendance = cls.get_attendance()
            if attendance == "Present":
                employee_type = cls.get_employee_type()
                if employee_type == "Full_time":
                    daily_work_hours = cls.FULL_TIME_HOUR
                else:
                    daily_work_hours = cls.PART_TIME_HOUR

                work_hour += daily_work_hours
                daily_wage = cls.employee_daily_wage(daily_work_hours)
                wage_list.append(daily_wage)
                total_wage += daily_wage
            else:
                wage_list.append(0)

            work_day += 1

        print("Wage list of Employee:")
        print(wage_list)
        print(f"Total wage: ${total_wage}")



def main():
    Employee.compute_monthly_wage()

if __name__ == "__main__":
    main()

