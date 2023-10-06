
from lib.cohort import Cohort
from lib.student import Student

class CohortRepository:

    def __init__(self, connection) -> None:
        self._connection = connection

    def all(self):
        rows = self._connection.execute('select * from cohorts')
        cohorts = []
        for row in rows:
            cohort = Cohort(row['id'], row['name'], row['starting_date'])
            cohorts.append(cohort)
        return cohorts

    def find(self, cohort_id):
        rows = self._connection.execute('select * from cohorts where id = %s', [cohort_id])
        row = rows[0]
        return Cohort(row['id'], row['name'], row['starting_date'])

    def find_with_students(self, cohort_id):

        query = """
                select 
                    cohorts.id as cohort_id, 
                    cohorts.name as cohort_name, 
                    cohorts.starting_date,
                    students.id as student_id,
                    students.name as student_name
                from 
                    cohorts 
                join
                    students
                on 
                    students.cohort_id = cohorts.id 
                where 
                    cohorts.id = %s 
                """

        rows = self._connection.execute(query,  [cohort_id])
        students = []
        for row in rows:
            student = Student(row['student_id'], row['student_name'], row['cohort_id'])
            students.append(student)
        return Cohort(rows[0]['cohort_id'], rows[0]['cohort_name'], rows[0]['starting_date'], students)
        
    def create(self):
        pass

    def delete(self):
        pass

    