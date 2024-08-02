"""
@Author: Girish
@Date: 2024-08-02
@Last Modified by: Girish
@Last Modified time: 2024-08-02
@Title: Ability to manage wage for multiple companies
"""

import random

class CompanyEmpWage:
    def __init__(self, company_name, wage_per_hour, full_time_hour, part_time_hour, working_day, total_working_hour):
        self.company_name = company_name
        self.wage_per_hour = wage_per_hour
        self.full_time_hour = full_time_hour
        self.part_time_hour = part_time_hour
        self.working_day = working_day
        self.total_working_hour = total_working_hour
        self.total_wage = 0
        self.wage_list = []

    def __str__(self):
        return (f"Company: {self.company_name}, Wage Per Hour: {self.wage_per_hour}, "
                f"Full Time Hour: {self.full_time_hour}, Part Time Hour: {self.part_time_hour}, "
                f"Working Day: {self.working_day}, Total Working Hour: {self.total_working_hour}, "
                f"Total Wage: {self.total_wage}, Wage List: {self.wage_list}")

class EmpWageBuilder:
    def __init__(self):
        self.company_emp_wage_list = []

    def add_company_emp_wage(self, company_emp_wage):
        self.company_emp_wage_list.append(company_emp_wage)

    def compute_wages(self):
        for company in self.company_emp_wage_list:
            self.compute_monthly_wage(company)

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    def compute_monthly_wage(self, company):
        """
        Description:
            Computes the total wage for the employee for the month for a specific company.

        Parameters:
            company (CompanyEmpWage): The company employee wage object

        Returns:
            None
        """
        self.display_welcome_message()
        print(f"Employee Wage for the month in {company.company_name}:")

        work_day = 1
        work_hour = 0
        total_wage = 0

        while work_hour <= company.total_working_hour and work_day <= company.working_day:
            attendance = self.get_attendance()
            if attendance == "Present":
                employee_type = self.get_employee_type()
                if employee_type == "Full_time":
                    daily_work_hours = company.full_time_hour
                else:
                    daily_work_hours = company.part_time_hour

                work_hour += daily_work_hours
                daily_wage = self.employee_daily_wage(company.wage_per_hour, daily_work_hours)
                company.wage_list.append(daily_wage)
                total_wage += daily_wage
            else:
                company.wage_list.append(0)

            work_day += 1

        company.total_wage = total_wage

        print("Wage list of Employee:")
        print(company.wage_list)
        print(f"Total wage in {company.company_name}: ${company.total_wage}")
        print("\n" + "="*80 + "\n")

def main():
    try:
        emp_wage_builder = EmpWageBuilder()

        emp_wage_builder.add_company_emp_wage(CompanyEmpWage("Google", 20, 8, 4, 20, 100))
        emp_wage_builder.add_company_emp_wage(CompanyEmpWage("Microsoft", 25, 9, 5, 22, 110))
        emp_wage_builder.add_company_emp_wage(CompanyEmpWage("Amazon", 30, 10, 6, 18, 90))
        emp_wage_builder.add_company_emp_wage(CompanyEmpWage("Apple", 35, 7, 3, 21, 95))

        emp_wage_builder.compute_wages()

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
