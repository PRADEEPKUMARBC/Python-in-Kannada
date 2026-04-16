class Student:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.__marks = {}
        self.name = name

    def add_marks(self, subject, marks):
        self.__marks[subject] = marks

    def get_marks(self):
        return self.__marks

    def calculate_average(self):
        total = 0
        for mark in self.__marks.values():
            total += mark
        average = total/len(self.__marks)
        return average

    def is_passed(self):
        # any() --> Atleast one true
        # all() -->  all True
        has_passed = all( mark < 35 for mark in self.__marks.values())
        if has_passed:
            print(f"{self.name} has passed")
        else:
            print(f"{self.name} has failed")

    def calculate_grade(self):
        print("Grade : ", end = "")
        percentage = self.calculate_average() * 100
        if percentage >= 90:
            print("A")
        elif percentage >= 80:
            print("B")
        elif percentage >= 75:
            print("C")
        else:
            print("D")
        
class ReportCard:
    @staticmethod
    def generate(student: Student):
        print(f" Name : {student.name} \t Roll_no : {student.roll_no}")
        print("---Marks--")
        for subject, marks in student.get_marks().items():
            print(f"{subject} - {marks}")
        print("------------------")
        print(f"Average : {student.calculate_average()}")
        student.is_passed()
        student.calculate_grade()

class ClassRoom:
    def __init__(self, grade, section):
        self.grade = grade
        self.section = section
        self.__students = []

    def add_student(self, student):
        self.__students.append(student) 
        
    def calculate_class_average(self):
        total = 0
        for student in self.__students(student):
            total += student
            average = total/len(self.__students)
        print(f" Average of the class is : {average}")

    def get_students_list(self):
        for i, student in self.__students:
            print(f" {student.roll_no} . {student.name}")

a = Student(1, "Akash")
a.add_marks("Math", 95)
a.add_marks("Science", 34)

ReportCard.generate(a)

c = ClassRoom("10", "B")
c.add_student(a)
b = Student(2, "Bharat")
c.add_student(b)
c.get_students_list()