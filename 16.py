
# Home work
# create class with constructor

class Movie:
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating

    def Display(self):
        print(f"the movies title is {self.title} and Movie rating is {self.rating}")
    
Movie1 = Movie("Toxic", 8.5)
Movie1.Display()



class Employe:
    def __init__(self, name, designation, salary = "150000"):
        self.name = name
        self.designation = designation
        self.salary = salary

    def Details(self):
        print(f" My Name is {self.name} and My designation is {self.designation} and My salary is {self.salary}")

Employe1 = Employe("Pradeep", "software Engieer", "200000")
Employe2 = Employe("Sanjay", "backend Engieer", )
Employe3 = Employe("Nagaraj", "frontend Engieer", )

Employe1.Details()
Employe2.Details()
Employe3.Details()