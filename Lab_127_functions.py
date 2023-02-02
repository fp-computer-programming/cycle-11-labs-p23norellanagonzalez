# author NDO 02/01/23

row = { 11: 'Nickolas Orellana',  12 : 'Ethan Forest' , 13 : 'Robbie Donahue', 14 : 'Jack Rydzik' }

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

var_sub = ['Geometry', 'Biology', 'English']
# Use a method to add a fourth subject to the end
var_sub.append('Religion')

# use a method to retun the index of one subject
ind_sub = var_sub.index('Biology')
print(ind_sub)

#Order the subjects alphabetically
var_sub.sort() 
print(var_sub)

# added a line of code to enumerate this list. 
obj1 = enumerate(var_sub)
print(enumerate(var_sub))

#Use a mathod to make a copy of the list 
copy_sub = var_sub[:]
# use a method to order this second list in reverse order
copy_sub.reverse()
print(copy_sub)

# create a variable and set it equal to the names of 2 people in your row 
my_row = ['Robbie', 'Ethan']
# Use slices and add your name at the end of the list 
my_row[2:3]= ['Nickolas']
print(my_row)

# create another variable and set it equal to the first row 
my_row2 = my_row 
print(my_row2)

# add a statement that removes the value at index 1 and then print the result
del my_row [1]
print(my_row)

# Create a list of 4 colors and sotre as a variable
four_colors = ['red', 'orange', 'yellow', 'green']
#Add 3 more colors to the list in a single statement
four_colors.extend(['blue', 'cyan', 'pink'])
# Use a different method to add one additional color 
four_colors.append('purple')
# Use a method to insert a new color at the index 3 
four_colors.insert(3,'turquoise')
print(four_colors)
# Use a method to create a copy of the list 
copy_colors = four_colors[:]
# Use a method to remove one element of the copy of the list 
del copy_colors[5]
print(copy_colors)

# Create a program that asks the user to input 5 words 
first_word = input('Please enter a word here ')
second_word = input('Please enter a word here ')
third_word = input('Please enter a word here ')
fourth_word = input('Please enter a word here ')
fifth_word = input('Please enter a word here ')

# Create list of the 5 previous input values in the order the user gave them
empt_list = [first_word, second_word, third_word, fourth_word, fifth_word]
print(empt_list)

# A program that displays the length of the index in the correspoding place of the input list
len_first = len(first_word)
len_second = len(second_word)
len_third= len(third_word)
len_fourth = len(fourth_word)
len_fifth = len(fifth_word)
len_list = [len_first, len_second, len_third, len_fourth, len_fifth]
print(len_list)
