"""
@Author: Girish
@Date: 2024-08-02
@Last Modified by: Girish
@Last Modified time: 2024-08-02
@Title: Ability to manage wage for multiple companies with CRUD operations for companies and employees
"""

import random

class Employee:
    def _init_(self, name):
        self.name = name
        self.total_wage = 0
        self.wage_list = []

    def _str_(self):
        return f"Employee: {self.name}, Total Wage: {self.total_wage}, Wage List: {self.wage_list}"

class CompanyEmpWage:
    def _init_(self, company_name, wage_per_hour, full_time_hour, part_time_hour, working_day, total_working_hour):
        self.company_name = company_name
        self.wage_per_hour = wage_per_hour
        self.full_time_hour = full_time_hour
        self.part_time_hour = part_time_hour
        self.working_day = working_day
        self.total_working_hour = total_working_hour
        self.employees = []

    def _str_(self):
        return (f"Company: {self.company_name}, Wage Per Hour: {self.wage_per_hour}, "
                f"Full Time Hour: {self.full_time_hour}, Part Time Hour: {self.part_time_hour}, "
                f"Working Day: {self.working_day}, Total Working Hour: {self.total_working_hour}, "
                f"Employees: {[str(emp) for emp in self.employees]}")

    def get_employee(self, employee_name):
        for employee in self.employees:
            if employee.name == employee_name:
                return employee
        return None

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee_name):
        self.employees = [emp for emp in self.employees if emp.name != employee_name]

    def update_employee(self, old_name, new_name):
        employee = self.get_employee(old_name)
        if employee:
            employee.name = new_name

class EmpWageBuilder:
    def _init_(self):
        self.company_emp_wage_list = []

    def add_company_emp_wage(self, company_emp_wage):
        self.company_emp_wage_list.append(company_emp_wage)

    def remove_company_emp_wage(self, company_name):
        self.company_emp_wage_list = [company for company in self.company_emp_wage_list if company.company_name != company_name]

    def update_company_emp_wage(self, old_company_name, new_company_emp_wage):
        for i, company in enumerate(self.company_emp_wage_list):
            if company.company_name == old_company_name:
                self.company_emp_wage_list[i] = new_company_emp_wage

    def get_company_emp_wage(self, company_name):
        for company in self.company_emp_wage_list:
            if company.company_name == company_name:
                return company
        return None

    def compute_wages(self):
        for company in self.company_emp_wage_list:
            for employee in company.employees:
                self.compute_monthly_wage(company, employee)

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

    def compute_monthly_wage(self, company, employee):
        """
        Description:
            Computes the total wage for the employee for the month for a specific company.

        Parameters:
            company (CompanyEmpWage): The company employee wage object
            employee (Employee): The employee object

        Returns:
            None
        """
        print(f"Computing wage for {employee.name} in {company.company_name}:")

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
                employee.wage_list.append(daily_wage)
                total_wage += daily_wage
            else:
                employee.wage_list.append(0)

            work_day += 1

        employee.total_wage = total_wage
        print(f"Wage list of {employee.name}:")
        print(employee.wage_list)
        print(f"Total wage for {employee.name} in {company.company_name}: ${employee.total_wage}")
        print("\n" + "="*80 + "\n")

def main():
    try:
        emp_wage_builder = EmpWageBuilder()

        while True:
            print("\n1. Add Company\n2. Update Company\n3. Delete Company\n4. Manage Employees\n5. Compute Wages\n6. Display Companies\n7. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                company_name = input("Enter company name: ")
                wage_per_hour = int(input("Enter wage per hour: "))
                full_time_hour = int(input("Enter full-time hours: "))
                part_time_hour = int(input("Enter part-time hours: "))
                working_day = int(input("Enter working days: "))
                total_working_hour = int(input("Enter total working hours: "))
                new_company = CompanyEmpWage(company_name, wage_per_hour, full_time_hour, part_time_hour, working_day, total_working_hour)
                emp_wage_builder.add_company_emp_wage(new_company)

            elif choice == "2":
                old_company_name = input("Enter the name of the company to update: ")
                if emp_wage_builder.get_company_emp_wage(old_company_name):
                    company_name = input("Enter new company name: ")
                    wage_per_hour = int(input("Enter new wage per hour: "))
                    full_time_hour = int(input("Enter new full-time hours: "))
                    part_time_hour = int(input("Enter new part-time hours: "))
                    working_day = int(input("Enter new working days: "))
                    total_working_hour = int(input("Enter new total working hours: "))
                    updated_company = CompanyEmpWage(company_name, wage_per_hour, full_time_hour, part_time_hour, working_day, total_working_hour)
                    emp_wage_builder.update_company_emp_wage(old_company_name, updated_company)
                else:
                    print("Company not found!")

            elif choice == "3":
                company_name = input("Enter the name of the company to delete: ")
                emp_wage_builder.remove_company_emp_wage(company_name)
                print(f"Company {company_name} removed.")

            elif choice == "4":
                company_name = input("Enter the name of the company to manage employees: ")
                company = emp_wage_builder.get_company_emp_wage(company_name)
                if company:
                    while True:
                        print("\n1. Add Employee\n2. Update Employee\n3. Delete Employee\n4. Compute Employee Wage\n5. Back to Main Menu")
                        emp_choice = input("Enter your choice: ")

                        if emp_choice == "1":
                            emp_name = input("Enter employee name: ")
                            new_employee = Employee(emp_name)
                            company.add_employee(new_employee)

                        elif emp_choice == "2":
                            old_emp_name = input("Enter the name of the employee to update: ")
                            new_emp_name = input("Enter new employee name: ")
                            company.update_employee(old_emp_name, new_emp_name)

                        elif emp_choice == "3":
                            emp_name = input("Enter the name of the employee to delete: ")
                            company.remove_employee(emp_name)
                            print(f"Employee {emp_name} removed from {company.company_name}.")

                        elif emp_choice == "4":
                            emp_name = input("Enter the name of the employee to compute wage: ")
                            employee = company.get_employee(emp_name)
                            if employee:
                                emp_wage_builder.compute_monthly_wage(company, employee)
                            else:
                                print("Employee not found!")

                        elif emp_choice == "5":
                            break

                        else:
                            print("Invalid choice! Please try again.")
                else:
                    print("Company not found!")

            elif choice == "5":
                emp_wage_builder.compute_wages()

            elif choice == "6":
                for company in emp_wage_builder.company_emp_wage_list:
                    print(company)

            elif choice == "7":
                break

            else:
                print("Invalid choice! Please try again.")

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()