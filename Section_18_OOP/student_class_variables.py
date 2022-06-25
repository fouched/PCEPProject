"""
Class variables
"""


class Student:
    school = 'Online School'
    number_of_students = 0

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

        Student.number_of_students += 1

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def full_name_school(self):
        return f'{self.first_name} {self.last_name} goes to {self.school}'


print(f'Number of students: {Student.number_of_students}')
student_1 = Student('Fouche', 'du Preez')
student_2 = Student('Emily', 'du Preez')
print(f'Number of students: {Student.number_of_students}')

print(student_1.school)
print(student_2.school)

print(Student.full_name_school(student_2))
