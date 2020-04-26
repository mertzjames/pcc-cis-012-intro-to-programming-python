

student_grades = {
    'Joe': [90, 95, 87, 99],
    'Sally': [97, 92, 90, 100],
    'Mark': [80, 83, 72, 89]
}

student_grades_avg = {}

def calc_avg(scores):
    avg = sum(scores) / len(scores)
    return avg

for student, scores in student_grades.items():
    student_grades_avg[student] = calc_avg(scores)
    
print(student_grades_avg)