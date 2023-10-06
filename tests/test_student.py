
from lib.student import Student

"""
test student object variables are initialised
"""
def test_student_initialisation():
    student = Student(1, 'test_student', 3)
    assert student.id == 1
    assert student.name == 'test_student'
    assert student.cohort_id == 3

def test_student_formatted_nicely():
    student = Student(1, 'test_student', 3)
    assert str(student) == 'Student(1, test_student, 3)'

def test_equality():
    student1 = Student(1, 'test_student', 3)
    student2 = Student(1, 'test_student', 3)
    assert student1 == student2