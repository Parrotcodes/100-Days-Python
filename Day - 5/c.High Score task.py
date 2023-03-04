#Highest Score in the class
#using for loop -> Method - 1
#using python methods -> Method -2 (max(),min())

#Method-1

print('Find the heighest score in the class? ')
student_scores = input('Enter the scores: ').split()

for n in range(0,len(student_scores)):
    student_scores[n]=int(student_scores[n])
print(student_scores)

#checking the heighest score from the list
highest_max = 0
for score in student_scores:
    if score>highest_max:
        highest_max=score

print(highest_max)


print(f'The highest score in the class is :{highest_max}')


#Method-2
print('Method-2 using max():')

top_score = max(student_scores)
print(top_score)
