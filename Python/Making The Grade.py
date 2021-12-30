def round_scores(student_scores):
    round_score = []
    while student_scores:
        round_score.append(round(student_scores.pop(0)))
    return round_score

def count_failed_students(student_scores):
    failed_students = 0
    for grade in student_scores:
        if grade <= 40:
            failed_students += 1
    return failed_students

def above_threshold(student_scores, threshold):
    best_scores = []
    for grade in student_scores:
        if grade >= threshold:
            best_scores.append(grade)
    return best_scores

def letter_grades(highest):
    grade_range = []
    for number in range(41, highest, round(((highest-41)/4))):
        grade_range.append(number)
    return grade_range

def student_ranking(student_scores, student_names):
    students_ranked = []
    for index, student in enumerate(student_names):
        rank = str(index+1) + ". " 
        students_ranked.append( rank + student + ": " + str(student_scores[index]))
    return students_ranked

def perfect_score(student_info):
    perfect_student = []
    for student in student_info:
        if student[1] == 100:
            return student
    return perfect_student