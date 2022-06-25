"""
Object Oriented Programming
"""


class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return f'{self.first_name} {self.last_name}'


# the self argument is automatically populated
student_1 = Student('Fouche', 'du Preez')
student_2 = Student('Emily', 'du Preez')

print(student_1.first_name)
print(student_2.first_name)

print(student_1.full_name())
# below is more popular
print(Student.full_name(student_2))
