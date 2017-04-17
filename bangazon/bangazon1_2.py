from bangazon import *

# Initialize Some Instances of Our Classes
print('Exercises 1 and 2:')
IS = Information_Systems_Dept()
print('Department Name: ' + IS.get_name())
print('Work From Home: ' + str(IS.WorkFromHome()))
print('Manager: ', IS.get_manager())
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




