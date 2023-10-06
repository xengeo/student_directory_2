from lib.cohort import Cohort

"""
test cohort initialises variables 
"""
def test_cohort_initialisation():
    cohort = Cohort(1, 'cohort_name', '2023-09-30')
    assert cohort.id == 1
    assert cohort.name == 'cohort_name'
    assert cohort.starting_date == '2023-09-30'

def test_cohort_formats_nicely():
    cohort = Cohort(1, 'cohort_name', '2023-09-30')
    assert str(cohort) == 'Cohort(1, cohort_name, 2023-09-30)'

def test_cohort_object_equality():
    cohort1 = Cohort(1, 'cohort_name', '2023-09-30')
    cohort2 = Cohort(1, 'cohort_name', '2023-09-30')
    assert cohort1 == cohort2