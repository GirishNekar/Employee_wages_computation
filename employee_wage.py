"""
@Author: Girish
@Date: 2024-08-01
@Last Modified by: Girish
@Last Modified time: 2024-08-01
@Title: Generating wage for 4 different companies
"""

import random

class EmployeeWage:
    @classmethod
    def display_welcome_message(cls):
        
        
        """
        Description:
            Prints the welcome message.

        Parameters:
            cls (type): The class on which this method is called

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
            cls (type): The class on which this method is called

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
            cls (type): The class on which this method is called

        Returns:
            str: "Present" if present, "Absent" if absent
        """
        
        
        return random.choice(["Present", "Absent"])



    @classmethod
    def employee_daily_wage(cls, wage_per_hour, work_hour):
        
        
        """
        Description:
            Calculates the employee's daily wage.

        Parameters:
            cls (type): The class on which this method is called
            wage_per_hour (int): Employee's wage per hour
            work_hour (int): Employee's working hours

        Returns:
            int: Daily wage
        """
        
        
        return work_hour * wage_per_hour



    @classmethod
    def compute_monthly_wage(cls, company_name, wage_per_hour, full_time_hour, part_time_hour, working_day, total_working_hour):
        
        
        """
        Description:
            Computes the total wage for the employee for the month for a specific company.

        Parameters:
            cls (type): The class on which this method is called
            company_name (str): Name of the company
            wage_per_hour (int): Wage per hour
            full_time_hour (int): Full-time working hours per day
            part_time_hour (int): Part-time working hours per day
            working_day (int): Number of working days in a month
            total_working_hour (int): Maximum allowable working hours in a month

        Returns:
            None
        """
        
        
        cls.display_welcome_message()
        print(f"Employee Wage for the month in {company_name}:")

        work_day = 1
        work_hour = 0
        wage_list = []
        total_wage = 0

        while work_hour <= total_working_hour and work_day <= working_day:
            attendance = cls.get_attendance()
            if attendance == "Present":
                employee_type = cls.get_employee_type()
                if employee_type == "Full_time":
                    daily_work_hours = full_time_hour
                else:
                    daily_work_hours = part_time_hour

                work_hour += daily_work_hours
                daily_wage = cls.employee_daily_wage(wage_per_hour, daily_work_hours)
                wage_list.append(daily_wage)
                total_wage += daily_wage
            else:
                wage_list.append(0)

            work_day += 1

        print("Wage list of Employee:")
        print(wage_list)
        print(f"Total wage in {company_name}: ${total_wage}")



def main():
    try:
        companies = [
            {"name": "Google", "wage_per_hour": 20, "full_time_hour": 8, "part_time_hour": 4, "working_day": 20, "total_working_hour": 100},
            {"name": "Microsoft", "wage_per_hour": 25, "full_time_hour": 9, "part_time_hour": 5, "working_day": 22, "total_working_hour": 110},
            {"name": "Amazon", "wage_per_hour": 30, "full_time_hour": 10, "part_time_hour": 6, "working_day": 18, "total_working_hour": 90},
            {"name": "Apple", "wage_per_hour": 35, "full_time_hour": 7, "part_time_hour": 3, "working_day": 21, "total_working_hour": 95},
        ]

        for company in companies:
            EmployeeWage.compute_monthly_wage(
                company_name=company["name"],
                wage_per_hour=company["wage_per_hour"],
                full_time_hour=company["full_time_hour"],
                part_time_hour=company["part_time_hour"],
                working_day=company["working_day"],
                total_working_hour=company["total_working_hour"]
            )
            print("\n" + "="*80 + "\n")

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
