from bangazon import *

# exercise 5
IS = Information_Systems_Dept()
HR = Human_Resources()
MRK = Marketing()

Tom = IS_Employee('Tom', 'Jones')
Jordan = IS_Employee('Jordan', 'Nelson')
Kathleen = IS_Employee('Kathleen', 'Elliott')
James = IS_Employee('James', 'Watterson')

IS.add_employee(Tom)
IS.add_employee(Jordan)
IS.add_employee(Kathleen)
IS.add_employee(James)

Sally = HR_Employee('Sally', 'Sals')
Keegan = HR_Employee('Keegan', 'Ronaldson')
Justin = HR_Employee('Justin', 'Foster')
Paula = HR_Employee('Paula', 'Thompson')

HR.add_employee(Sally)
HR.add_employee(Keegan)
HR.add_employee(Justin)
HR.add_employee(Paula)

Billy = MRK_Employee('Billy', 'Petroski')
Paul = MRK_Employee('Paul', 'McDonald')
Jean = MRK_Employee('Jean', 'Ruthero')

MRK.add_employee(Billy)
MRK.add_employee(Paul)
MRK.add_employee(Jean)


IS.get_employees()
HR.get_employees()
MRK.get_employees()
