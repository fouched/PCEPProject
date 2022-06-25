"""
Class methods
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

    @classmethod
    def set_online_school(cls, new_school):
        cls.school = new_school

    @classmethod
    def split_students(cls, student_str):
        first_name, last_name = student_str.split('.')
        # object - instance of the class
        return cls(first_name, last_name)


print(f'Number of students: {Student.number_of_students}')
student_1 = Student('Fouche', 'du Preez')
student_2 = Student('Emily', 'du Preez')
print(f'Number of students: {Student.number_of_students}')

print(student_1.school)
print(student_2.school)

# NOTE!!! this changes the value for all objects!
student_1.set_online_school('Udemy')
print(student_1.school)
print(student_2.school)
# it is the same as doing
Student.set_online_school('Gelofte')
print(student_1.school)
print(student_2.school)

new_student = 'Olivia.du Preez'
student_3 = Student.split_students(new_student)
print(student_3.full_name_school())

print(Student.full_name_school(student_2))
