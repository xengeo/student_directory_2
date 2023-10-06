from lib.database_connection import DatabaseConnection
# from lib.artist_repository import ArtistRepository
from lib.cohort_repository import CohortRepository

# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/student_directory_2.sql")

# # Retrieve all artists
# artist_repository = ArtistRepository(connection)
# artists = artist_repository.all()

# # List them out
# for artist in artists:
#     print(artist)

cohort_repository = CohortRepository(connection)
cohort = cohort_repository.find_with_students(3)
print(cohort)
formatted_students = '\n\t'.join(student.name for student in cohort.students)
print(f"{cohort.name} contains the following students:\n\t{formatted_students}")