

class Cohort:

    def __init__(self, id, name, starting_date, students = None) -> None:
        self.id = id
        self.name = name 
        self.starting_date = str(starting_date)
        self.students = students or []

    def __eq__(self, other: object) -> bool:
        return self.__dict__ == other.__dict__

    def __repr__(self) -> str:
        if self.students:
            return f'Cohort({self.id}, {self.name}, {self.starting_date}, {self.students})'
        return f'Cohort({self.id}, {self.name}, {self.starting_date})'


