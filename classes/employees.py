class Employee(object):
	"""This represents employees which work for a company"""

	def __init__(self, name, title, start_date):
		self.name = name
		self.title = title
		self.start_date = start_date

	def get_name(self):
		"""Returns the name of the employee"""
		return self.name

	def get_title(self):
		"""Returns the employee's job title"""
		return self.title

	def get_start_date(self):
		"""Returns the employee's start date"""
		return self.start_date

class Company(object):
    """This represents a company in which people work"""

    def __init__(self, name):
        self.name = name
        self.title = ""
        self.start_date = ""
        self.employee = set()

    def get_name(self):
        """Returns the name of the company"""
        return self.name


jordan = Employee("Jordan", "CEO", "1/1/1985")

JordanCorp = Company("JordanCorp")
JordanCorp.employee.add(jordan)


print(JordanCorp.get_name())
print(jordan.name, jordan.title, jordan.start_date)


