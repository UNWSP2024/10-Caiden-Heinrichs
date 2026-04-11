#Week 10, Program 4 - Employee Class
#Caiden Heinrichs
#04/10/26

class Employee:
    #Initiate attributes
    def __init__(self, name, idNumber, department, jobTitle):
        self.name = name
        self.idNumber = idNumber
        self.department = department
        self.jobTitle = jobTitle


def main():
    #Create employee objects
    employee1 = Employee('Susan Meyers', '47899', 'Accounting', 'Vice President')
    employee2 = Employee('Mark Jones', '39119', 'IT', 'Programmer')
    employee3 = Employee('Joy Rogers', '81774', 'Manufacturing', 'Engineer')

    #Print employee information
    print(f'First employee name: {employee1.name}')
    print(f'First employee ID: {employee1.idNumber}')
    print(f'First employee department: {employee1.department}')
    print(f'First employee job title: {employee1.jobTitle}', end='\n\n')

    print(f'Second employee name: {employee2.name}')
    print(f'Second employee ID: {employee2.idNumber}')
    print(f'Second employee department: {employee2.department}')
    print(f'Second employee job title: {employee2.jobTitle}', end='\n\n')

    print(f'Third employee name: {employee3.name}')
    print(f'Third employee ID: {employee3.idNumber}')
    print(f'Third employee department: {employee3.department}')
    print(f'Third employee job title: {employee3.jobTitle}')


if __name__ == '__main__':
    main()
