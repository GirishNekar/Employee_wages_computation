"""
@Author: Girish
@Date: 2024-08-02
@Last Modified by: Girish
@Last Modified time: 2024-08-02
@Title: Saving  wage for 4 different companies that are generated
"""

import random

class EmployeeWage:
    def __init__(self, company_name, wage_per_hour, full_time_hour, part_time_hour, working_day, total_working_hour):
        self.company_name = company_name
        self.wage_per_hour = wage_per_hour
        self.full_time_hour = full_time_hour
        self.part_time_hour = part_time_hour
        self.working_day = working_day
        self.total_working_hour = total_working_hour
        self.wage_list = []
        self.total_wage = 0

    def display_welcome_message(self):
        """
        Description:
            Prints the welcome message.

        Parameters:
            None

        Returns:
            None
        """
        print(f"Hello Everyone, welcome to Employee Wage Computation at {self.company_name}")

    def get_employee_type(self):
        """
        Description:
            Returns whether the employee is working part-time or full-time.

        Parameters:
            None

        Returns:
            str: "Part_time" or "Full_time"
        """
        return random.choice(["Part_time", "Full_time"])

    def get_attendance(self):
        """
        Description:
            Determines if the employee is present or absent.

        Parameters:
            None

        Returns:
            str: "Present" if present, "Absent" if absent
        """
        return random.choice(["Present", "Absent"])

    def employee_daily_wage(self, work_hour):
        """
        Description:
            Calculates the employee's daily wage.

        Parameters:
            work_hour (int): Employee's working hours

        Returns:
            int: Daily wage
        """
        return work_hour * self.wage_per_hour

    def compute_monthly_wage(self):
        """
        Description:
            Computes the total wage for the employee for the month for a specific company.

        Parameters:
            None

        Returns:
            None
        """
        self.display_welcome_message()
        print(f"Employee Wage for the month in {self.company_name}:")

        work_day = 1
        work_hour = 0

        while work_hour <= self.total_working_hour and work_day <= self.working_day:
            attendance = self.get_attendance()
            if attendance == "Present":
                employee_type = self.get_employee_type()
                if employee_type == "Full_time":
                    daily_work_hours = self.full_time_hour
                else:
                    daily_work_hours = self.part_time_hour

                work_hour += daily_work_hours
                daily_wage = self.employee_daily_wage(daily_work_hours)
                self.wage_list.append(daily_wage)
                self.total_wage += daily_wage
            else:
                self.wage_list.append(0)

            work_day += 1

        self.print_wage_details()

    def print_wage_details(self):
        """
        Description:
            Prints the wage list and total wage for the company.

        Parameters:
            None

        Returns:
            None
        """
        print("Wage list of Employee:")
        print(self.wage_list)
        print(f"Total wage in {self.company_name}: ${self.total_wage}")


class EmpWageBuilder:
    def __init__(self):
        self.companies = []
        self.total_wages = {}

    def add_company(self, company_name, wage_per_hour, full_time_hour, part_time_hour, working_day, total_working_hour):
        company = EmployeeWage(company_name, wage_per_hour, full_time_hour, part_time_hour, working_day, total_working_hour)
        self.companies.append(company)

    def compute_wages(self):
        for company in self.companies:
            company.compute_monthly_wage()
            self.total_wages[company.company_name] = company.total_wage
            print("\n" + "="*80 + "\n")

    def print_total_wages(self):
        """
        Description:
            Prints the total wage for each company.

        Parameters:
            None

        Returns:
            None
        """
        print("Total wages for each company:")
        for company_name, total_wage in self.total_wages.items():
            print(f"{company_name}: ${total_wage}")


def main():
    try:
        emp_wage_builder = EmpWageBuilder()
        
        emp_wage_builder.add_company("Google", 20, 8, 4, 20, 100)
        emp_wage_builder.add_company("Microsoft", 25, 9, 5, 22, 110)
        emp_wage_builder.add_company("Amazon", 30, 10, 6, 18, 90)
        emp_wage_builder.add_company("Apple", 35, 7, 3, 21, 95)

        emp_wage_builder.compute_wages()
        emp_wage_builder.print_total_wages()

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
