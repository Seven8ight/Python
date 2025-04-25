# Calculate the average for students and output 2 if name == 'John'
import math

def averages(marks:list[int]) -> int:
    sum:int = 0

    for mark in marks:
        sum += mark

    return math.floor(sum / len(marks))

students:list[dict] = [
    {"student_name":"Alice","Marks":[99,85,68]},
    {"student_name":"Bob","Marks":[99,90,56]},
    {"student_name":"Jane","Marks":[99,90,56]},
    {"student_name":"John","Marks":[90,87,65]}
]

for student in students:
    for attribute in student:
        if(attribute == 'student_name'):
            print(f'Student name: {student[attribute]}')
            
            if(student[attribute] == 'John'):
                print("John here")
        else:
            print(f'Average marks: {averages(student[attribute])}\n')