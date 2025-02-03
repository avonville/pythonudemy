import random

numbers = [1,2,3]
new_numbers = [n+1 for n in numbers]
print( new_numbers )

name = "Angela"
new_list = [ letter for letter in name]
print( new_list )

range_list = [n*2 for n in range(1,5)]
print( range_list )

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
cap_names = [n.upper() for n in names if len(n) > 5]
print(cap_names)

student_scores = {student:random.randint(1,100) for student in names}
print(student_scores)

passed_students = {student:score for student, score in student_scores.items() if score >= 60}
print(passed_students)
