class Student:

    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1


student1 = Student("SpongeBob", 30)
student2 = Student("Patrick", 40)

print(student1.name)
print(student1.age)
print(student2.name)
print(student2.age)
print(Student.class_year)
print(Student.class_year)

print(Student.num_students)
print(Student.num_students)
student3 = Student("Squidward", 55)
print(
    Student.num_students
)  # Counter which will be incremented based on how many objects are created for the class!
