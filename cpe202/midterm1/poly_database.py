"""Classes for Student and Course.
Course: CPE202
Quarter: Spring 2020
Author: Henry Berman
"""


class Course:
    """A course that a Cal Poly student can take
    Attributes:
        name (str): name of course
        grade (str): grade student recieved
    """
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


class Student:
    """A student at Cal Poly
    Attributes:
        last_name (str): last name of student
        first_name (str): first name of student
        major (str): major of student
        grad_date (str): YYYY expected graduation date
        courses (list): list of Courses student has take
    """
    def __init__(self, ln, fn, maj, grad, courses):
        self.last_name = ln
        self.first_name = fn
        self.major = maj
        self.grad_date = grad
        self.courses = courses


# example code
c1 = Course('CPE202', 'A')
c2 = Course('PHYS132', 'B')
c3 = Course('MATH244', 'C')
courses = [c1, c2, c3]
student1 = Student('Berman', 'Henry', 'Computer Science', '2023', courses)
