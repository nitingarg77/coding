

class Student:

    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Niitn",24)
student2 = Student("Sachin", 21)
student3 = Student("Kapil", 18)

print(student1.name)
print(Student.class_year)
print(Student.num_students)