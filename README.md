###Salma Shnur 101315794
This assignment implements a PostgreSQL database using the given schema and an application that connects to this database to perform CRUD operations.

A video demonstrating the execution of all CRUD operations using the python file with a voice overlay is at: [link](https://drive.google.com/file/d/1LUYY0Iipk_oepgVBgmDT0EgSBBXkO0VC/view?usp=sharing)

###Database Schema:

```
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    enrollment_date DATE
);

INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');
```
###Application Functions:

- getAllStudents(): retrieves and shows all students in the table
- addStudent(first_name, last_name, email, enrollment_date): adds a student to the table
- updateStudentEmail(student_id, new_email): updates the email address of the  student
- deleteStudent(student_id): deletes the student with the student id

###Compilation Instructions:
- navigate to the directory that includes the student.py utilzing cd
- then run ```python student.py``` to see the output of the python file 


