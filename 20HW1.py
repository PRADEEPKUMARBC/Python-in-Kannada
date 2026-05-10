class Student:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name
        self.__marks = {}

    def get_marks(self):
        return self.__marks

    def add_marks(self, subjects, marks):
        self.__marks[subjects] = marks

    def calculate_average(self):
        total = 0
        for subjects , marks, in self.__marks.items():
            total += marks
            average = total/(len(self.__marks))
        return average

    def is_passed(self):
        has_passed = all( mark > 35 for mark in self.__marks.values())
        if has_passed:
            print(f"{self.name} is passed")
        else:
            print(f" {self.name} is failed")

    def calculate_grade(self):
        # TODO : fix this issue
        percentage = self.calculate_average() * 100
        if percentage == 95:
            print("Grade A")
        elif percentage == 80:
            print("Grade B")
        else:
            print("Grade C")

class ReportCard:
    @staticmethod
    def generate(student: Student):
        student_marks = student.get_marks()
        print(f"Name : {student.name} \t Roll No : {student.roll_no}")
        print("-----Marks-----")
        for subject, marks in student_marks.items():
            print(f"{subject} - {marks}")
        print("----------")
        print(f"Average : {student.calculate_average()}")
        student.is_passed()
        student.calculate_grade()

class ClassRoom:
    def __init__(self, grade, section):
        self.__students = []

    def add_student(self, student):
        self.__students.append(student)

    def calculate_class_average(self):
        pass

    def get_student_list(self):
        for i, student in enumerate(self.__students):
            print(f" {i+1} {student.name}")

a = Student(1, "Pradeep")
a.add_marks("Math", 95)
a.add_marks("Science", 34)

c = ClassRoom("10", "B")
c.add_student(a)

ReportCard.generate(a)

