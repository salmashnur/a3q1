import psycopg2
from psycopg2 import sql

#database connection
def connect():
    return psycopg2.connect(
        host="localhost",
        database="a3",
        user="salma",
        password="password"
    )

#takes and displays all students from the database
def getAllStudents():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students;")
    students = cur.fetchall()
    print("\nStudents:")
    for student in students:
        print(student)
    cur.close()
    conn.close()

#adds a student to the database
def addStudent(first_name, last_name, email, enrollment_date):
    conn = connect()
    cur = conn.cursor()
    try:
        cur.execute("""
            INSERT INTO students (first_name, last_name, email, enrollment_date)
            VALUES (%s, %s, %s, %s);
        """, (first_name, last_name, email, enrollment_date))
        conn.commit()
        print(f"Student {first_name} {last_name} added.")
    except psycopg2.Error as e:
        print("Error adding:", e)
    finally:
        cur.close()
        conn.close()

#updates the email with the student_id
def updateStudentEmail(student_id, new_email):
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        UPDATE students
        SET email = %s
        WHERE student_id = %s;
    """, (new_email, student_id))
    conn.commit()
    if cur.rowcount > 0:
        print("Email updated.")
    else:
        print("Student does not exist.")
    cur.close()
    conn.close()

#deletes a student record with the student_id
def deleteStudent(student_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE student_id = %s;", (student_id,))
    conn.commit()
    if cur.rowcount > 0:
        print("Student deleted.")
    else:
        print("Student not found.")
    cur.close()
    conn.close()

#utilizing the CRUD methods!!!
if __name__ == "__main__":
    print("Initial students:")
    getAllStudents()

    print("\nAdding salma:")
    addStudent("Salma", "Shnur", "salmashnur@gmail.com", "2023-09-07")

    print("\nStudent table after adding:")
    getAllStudents()

    print("\nUpdating johns email:")
    updateStudentEmail(1, "new.john.email@gmail.com")

    print("\nStudent table after update:")
    getAllStudents()

    print("\nDeleting student:")
    deleteStudent(3)

    print("\nStudent table after deletion:")
    getAllStudents()
