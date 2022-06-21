def calc_homework(homework):
    sum_of_grades = 0
    for x in homework.values():
        sum_of_grades += x
    final_grade = round(sum_of_grades / len(homework), 2)
    print(final_grade)
