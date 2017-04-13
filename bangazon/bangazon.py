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

	def override_me(self):
		print('Over-Ride Me Please')

	# Default budget set here
	def get_budget(self):
		self.budget = 1000
		return self.budget

## Information Systems Class
class Information_Systems_Dept(Department):

	def __init__(self):
		# no need for super as we're inheriting from one class
		Department.__init__(self, 'Information Systems', 'Joe', 25)
		super(Information_Systems_Dept, self).get_budget()
		self.work_from_home = True

	def get_budget(self):
		self.budget += 10000
		return self.budget

	def WorkFromHome(self):
		return self.work_from_home

## Human Resources Class
class Human_Resources(Department):

	def __init__(self):
		Department.__init__(self, 'Human Resources', 'Bob', 10)
		super(Human_Resources, self).get_budget()
		self.employee_list = set()
		self.isHated = True

	def get_budget(self):
		self.budget -= 200
		return self.budget

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

	def __init__(self):
		Department.__init__(self, 'Marketing', 'Jane', 6)
		super(Marketing, self).get_budget()

	def get_budget(self):
		self.budget += 5000
		return self.budget

	def override_me(self):
		print('I am over-ridden in Marketing but now in HR')

class Employee(object):

	def __init__(self, first_name, last_name):
		self.firstname = first_name
		self.lastname = last_name

	def get_name(self):
		print(self.firstname + ' ' + self.lastname)

Joe = Employee('Bob', 'Smithers')
Joe.get_name()



# Initialize Some Instances of Our Classes
IS = Information_Systems_Dept()
print('Department Name: ' + IS.get_name())
print('Work From Home: ' + str(IS.WorkFromHome()))
print('Manager: ', IS.get_manager())
print('Employees: {}'.format(IS.get_employees()))
print('Budget Is: ' + str(IS.get_budget()) )

print(' ')

HR = Human_Resources()
print('Department Name: ' + HR.get_name())
print('Budget is: ' + str(HR.get_budget()) )
print('Are they Hated? ', HR.DeptHated())
HR.add_employee_name('Parker')
HR.add_employee_name('Slimer')
HR.add_employee_name('Calbert')
print('List of Employee Names Added: ' + str(HR.get_employee_list()))
HR.override_me()

print(' ')

MRK = Marketing()
print('Department Name: ' + MRK.get_name())
print('Budget is: ' + str(MRK.get_budget()) )
MRK.override_me()




