import random

class Department(object):

	def __init__(self, name, manager):
		self.name = name
		self.manager = manager
		self.employees = set()

	def get_name(self):
		return self.name

	def get_manager(self):
		return self.manager

	def override_me(self):
		print('Over-Ride Me Please')

	# Default budget set here
	def get_budget(self):
		self.budget = 1000
		return self.budget

	# for exercise 5
	def add_employee(self, employee):
		self.employees.add(employee)

	def remove_employee(self, employee):
		self.employees.remove(employee)

	def get_employees(self):
		print('-------------------------')
		print('Department Name:', self.name )
		print('Manager: ', self.get_manager() )
		print('Budget: ', self.get_budget() )
		print(' ')
		for x in self.employees:
			print('Employee: ', x.firstname, x.lastname)
			print('Hours Per Week: ', x.hours_per_week)
			print('Location: ', x.location)
			print(' ')

## Information Systems Class
class Information_Systems_Dept(Department):

	def __init__(self):
		# no need for super as we're inheriting from one class
		Department.__init__(self, 'Information Systems', 'Joe')
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
		Department.__init__(self, 'Human Resources', 'Bob')
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
		Department.__init__(self, 'Marketing', 'Jane')
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

	def eat(self, food=None, companions=None):
		restaraunts = [ 'Outback', 'Burger King', 'McDonalds', '3 Crow', 'Melrose', 'Applebees', 'KFC', 'Panera']
		random_restaraunt = random.choice(restaraunts)

		if food is None and companions is None:
			print('{} {} ate at {}'.format(self.firstname, self.lastname, random_restaraunt))
		elif food is not None and companions is None:
			print('{} {} ate a {} at the Office'.format(self.firstname, self.lastname, food))
		elif food is None and companions is not None:
			print('{} {} ate at {} with {}'.format(self.firstname, self.lastname, random_restaraunt, ', '.join(companions)))
		elif food is not None and companions is not None:
			print('{} {} ate at {} and ordered {} with {}'.format(self.firstname, self.lastname, random_restaraunt, food, ', '.join(companions)))

class FullTime(object):

	def __init__(self):
		self.hours_per_week = 40

class PartTime(object):

	def __init__(self):
		self.hours_per_week = 24

class LocationA(object):

	def __init__(self):
		self.location = 'Annex'

class LocationB(object):

	def __init__(self):
		self.location = 'Sunnyvale Office'

class IS_Employee(Employee, FullTime, LocationA):

	def __init__(self, first_name, last_name):
		Employee.__init__(self, first_name, last_name)
		FullTime.__init__(self)
		LocationA.__init__(self)

class HR_Employee(Employee, PartTime, LocationB):

	def __init__(self, first_name, last_name):
		Employee.__init__(self, first_name, last_name)
		PartTime.__init__(self)
		LocationB.__init__(self)

class MRK_Employee(Employee, FullTime, LocationA):

	def __init__(self, first_name, last_name):
		Employee.__init__(self, first_name, last_name)
		FullTime.__init__(self)
		LocationA.__init__(self)

