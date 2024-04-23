'''
Create a function that takes a student's name and their scores in different subjects as input.
The function calculates the average score and prints the student's name, average, and a message 
indicating whether the student passed the exam (average >= 60) or failed.
Create a for loop to iterate over a list of students and scores, calling the function for each student.
'''

#students=[{student_name:{subject_1:grade, subject_2:grade, ...}}]
students=[('Paperino', {'math':20, 'geography':30, 'english':60}), 
          ('Pippo', {'math':50, 'geography':60, 'english':70}), 
          ('Pluto', {'math':100, 'geography':100, 'english':100}),
          ('Gastone', {'math':0, 'geography':0, 'english':0})
          ]

#calculates average number given numbers list
def average(numbers: list):
    dummy=sum(numbers)
    return dummy//len(numbers)

#main
def student_grading(student_name, student_grades: dict):
    grades=[value for value in student_grades.values()]
    if average(grades)>=60:
        return f'{student_name}, final grade: {average(grades)}.\nCongratulations, you passed!'
    else:
        return f'{student_name}, final grade: {average(grades)}.\nI\'m sorry, you didn\'t pass.'

#init
for student, grade in students:
    print(student_grading(student, grade))