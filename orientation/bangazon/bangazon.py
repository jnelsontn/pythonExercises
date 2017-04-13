## All Departments Inherit from Department
class Department(object):

	def __init__(self, name, manager, employees):
		self.name = name
		self.manager = manager
		self.employees = employees

	def get_name(self):
		return self.name

	def get_manager(self):
		return self.manager

	def get_employees(self):
		return self.employees

	def add_employees(self, x):
		self.employees += x

## Information Systems Class
class Information_Systems_Dept(Department):

	def __init__(self):
		Department.__init__(self, 'Information Systems', 'Joe', 25)
		self.work_from_home = True

	def WorkFromHome(self):
		return self.work_from_home

## Human Resources Class
class Human_Resources(Department):

	def __init__(self):
		Department.__init__(self, 'Human Resources', 'Bob', 10)
		self.employee_list = set()
		self.isHated = True

	def DeptHated(self):
		return self.isHated

	def add_employee_name(self, employee_name):
		self.employee_list.add(employee_name)

	def remove_employee(self, name):
		self.employee_list.remove(name)

	def get_employee_list(self):
		return self.employee_list

## Marketing Class
class Marketing(Department):

	def __init__(self, budget):
		Department.__init__(self, 'Marketing', 'Jane', 6)
		self.budget = budget

	def change_budget(self, x):
		self.budget = x

	def get_budget(self):
		return self.budget



# Initialize Some Instances of Our Classes
IS = Information_Systems_Dept()
print('Department Name: ' + IS.get_name())
print('Work From Home: ' + str(IS.WorkFromHome()))
print('Manager', IS.get_manager())
print('Employees: {}'.format(IS.get_employees()))

print(' ')

HR = Human_Resources()
print('Department Name: ' + HR.get_name())
print('Are they Hated? ', HR.DeptHated())
HR.add_employee_name('Parker')
HR.add_employee_name('Slimer')
HR.add_employee_name('Calbert')
print('List of Employee Names Added: ' + str(HR.get_employee_list()))

print(' ')

MRK = Marketing(3000)
print('Department Name: ' + MRK.get_name())
print('Budget: ' + str(MRK.get_budget()) )
MRK.change_budget(5000)
print('Budget is Now: ' + str(MRK.get_budget()) )
