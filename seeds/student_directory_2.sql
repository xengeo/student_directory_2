
DROP TABLE IF EXISTS students;
DROP SEQUENCE IF EXISTS students_id_seq;
DROP TABLE IF EXISTS cohorts;
DROP SEQUENCE IF EXISTS cohorts_id_seq;


-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS cohorts_id_seq;
CREATE TABLE cohorts (
  id SERIAL PRIMARY KEY,
  name text,
  starting_date date
);

CREATE SEQUENCE IF NOT EXISTS students_id_seq;
CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  name text,
  cohort_id int,
  constraint fk_cohort foreign key(cohort_id) references cohorts(id) on delete cascade
);

INSERT INTO cohorts (id, name, starting_date) VALUES (1, 'cohort_1', '2023-09-01');
INSERT INTO cohorts (id, name, starting_date) VALUES (2, 'cohort_2', '2023-09-02');
INSERT INTO cohorts (id, name, starting_date) VALUES (3, 'cohort_3', '2023-09-03');

INSERT INTO students (id, name, cohort_id) VALUES (1, 'student1', 1);
INSERT INTO students (id, name, cohort_id) VALUES (2, 'student2', 2);
INSERT INTO students (id, name, cohort_id) VALUES (3, 'student3', 3);
INSERT INTO students (id, name, cohort_id) VALUES (4, 'student4', 3);
INSERT INTO students (id, name, cohort_id) VALUES (5, 'student5', 2);
INSERT INTO students (id, name, cohort_id) VALUES (6, 'student6', 1);