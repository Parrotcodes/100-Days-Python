#Loops in Python
#Avg Height Exercise

student_heights = input('Input a list of students:').split()

#Taking every height as a list form
for n in range(0,len(student_heights)):
    student_heights[n] = int(student_heights[n])

print(student_heights)

#finding the sum() of list items by looping the list-items
total_height = 0
for height in student_heights:
    total_height += height
print(f'Sum of all students heights:{total_height}')

#finding the len() of list items by for-loop
total_students = 0
for student in student_heights:
    total_students += 1

print(f'Total number of students: {total_students}')

#Average of student_heights in the lists

Avg = round(total_height / total_students)
print(f'The average Height from the input heights is {Avg}')


            #--------*****---------

#Method  - 2 using sum() and len() methods

t_height = sum(student_heights)
t_n_students = len(student_heights)
avg_height = round(t_height/t_n_students)

print(t_height)
print(t_n_students)
print(avg_height)


