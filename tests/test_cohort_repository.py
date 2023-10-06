from lib.cohort_repository import CohortRepository
from lib.cohort import Cohort
from lib.student import Student

"""
test cohortrepository#all returns all
cohorts based on seeded data
"""
def test_all_method_returns_all_cohorts(db_connection):
    db_connection.seed('seeds/student_directory_2.sql')
    repository = CohortRepository(db_connection)

    cohorts = repository.all()
    assert cohorts == [
        Cohort(1, 'cohort_1', '2023-09-01'),
        Cohort(2, 'cohort_2', '2023-09-02'),
        Cohort(3, 'cohort_3', '2023-09-03')
        ]
    

"""
test find method finds relevant cohort
using cohort id
"""
def test_find_method_returns_cohort_object(db_connection):
    db_connection.seed('seeds/student_directory_2.sql')
    repository = CohortRepository(db_connection)
    cohort = repository.find(1)
    assert cohort == Cohort(1, 'cohort_1', '2023-09-01')


"""
test find_with_students returns a cohort with
the students arritbute with associateed students (using join query)
"""
def test_find_with_students_returns_cohort_with_students_list(db_connection):
    db_connection.seed('seeds/student_directory_2.sql')
    repository = CohortRepository(db_connection)
    cohort = repository.find_with_students(2) #arg is cohort id
    assert cohort == Cohort(2, 'cohort_2', '2023-09-02', [Student(2, 'student2', 2), Student(5, 'student5', 2)])