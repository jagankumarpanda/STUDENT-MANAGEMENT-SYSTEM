import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        ssl_ca="ca.pem",
        ssl_verify_cert=True
    )

def create_table():
    connection = get_connection()
    cursor = connection.cursor()

    query = """
        CREATE TABLE IF NOT EXISTS STUDENTS(
            ID INT AUTO_INCREMENT PRIMARY KEY,
            NAME VARCHAR(100) NOT NULL,
            COURSE VARCHAR(100) NOT NULL,
            FEE DECIMAL(10,2) NOT NULL
        )
    """
    cursor.execute(query)
    cursor.close()
    connection.close()
    print("Student Table is Ready....")


def create_student(student):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO STUDENTS(name, course, fee) VALUES(%s, %s, %s)"
    cursor.execute(query, (student.name, student.course, student.fee))

    conn.commit()
    cursor.close()
    conn.close()
    return {"success": True, "Message": "Student Created", "data": student}


def get_students():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM STUDENTS"

    cursor.execute(query)
    students = cursor.fetchall()

    cursor.close()
    conn.close()

    return {
        "success": True,
        "Message": "Student fetched successfully",
        "data": students,
    }


def get_student_by_id(id: int):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM STUDENTS WHERE ID = %s"
    cursor.execute(query, (id,))
    student = cursor.fetchone()
    cursor.close()
    conn.close()

    if student:
        return {"success": True, "message": "Student found", "data": student}
    else:
        return {"success": False, "message": "Student not found", "data": None}


def update_student(id: int, student):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE STUDENTS SET name = %s, course = %s, fee = %s WHERE ID = %s"
    cursor.execute(query, (student.name, student.course, student.fee, id))

    conn.commit()
    cursor.close()
    conn.close()

    return {"success": True, "message": "Student updated", "data": student}


def delete_student(id: int):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM STUDENTS WHERE ID = %s"
    cursor.execute(query, (id,))

    conn.commit()
    cursor.close()
    conn.close()

    return {"success": True, "message": "Student deleted"}