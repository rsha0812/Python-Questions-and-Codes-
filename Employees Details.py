print("Enter number of employees: ")
x = int(input())
employee = []

for i in range(x):
	print(" Enter the details of employee", i+1)
	name=input("Enter the names of employees: ")
	age = int(input(" Enter the age of employees: "))
	ID = int(input(" Enter the employees ID: "))
	Department = input("Enter the department: ")
	Salary = int(input("Enter the salary: "))
	emp = {'names':name, 'ages':age, 'IDs': ID, 'Dept': Department,'Sal': Salary}
	employee.append(emp)

def printTable(emploi):
	print("--------------------------------------------------------")
	print(" Name 		Age 		ID 		Dept 		Sal")
	for i in range(len(emploi)):
		print(emploi[i]['names'],"		",emploi[i]['ages'],"		",emploi[i]['IDs'],"		",emploi[i]['Dept'],"		",emploi[i]['Sal'])
		print("--------------------------------------------------------")
	print("--------------------------------------------------------")

printTable(employee)