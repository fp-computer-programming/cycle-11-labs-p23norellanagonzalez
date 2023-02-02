# author NDO 01/31/23 

# created a dictionary named grades that contains keys for each assignment of the quarter, as well as, the grade out of 100 
grades = {'Mid-year Project Presentation': 86/100, 'Mid-year Project Proposal': 80/100, 'Mid-year Project Code': 94/100, 'Mid-year Project Reflection': 86/100}
# one-line statement that prints all the grades
print(grades)

# Use a loop to print the name of the assignments
for k in grades: 
    print(k)

#Use another loop to print the name of the assignments that you scored a 70 or above 
for (k,v) in grades.items():
    print('In the assignment', k, "I received a 70 or above of :", v)