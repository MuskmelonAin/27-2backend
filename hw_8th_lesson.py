import sqlite3
from abc import ABC, abstractmethod

class DatabaseModel(ABC):
    _connection = None

    @classmethod
    def connect(cls, db_name='university.db'):
        cls._connection = sqlite3.connect(db_name)
    
    @classmethod
    def close(cls):
        if cls._connection:
            cls._connection.close()
    
    @abstractmethod
    def save_to_db(self):
        pass
    
    @abstractmethod
    def info(self):
        pass

class Person(ABC):
    def init(self, full_name, age):
        self.__full_name = full_name
        self.__age = age
    
    @property
    def full_name(self):
        return self.__full_name
    
    @full_name.setter
    def full_name(self, value):
        self.__full_name = value
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        self.__age = value

class Student(Person, DatabaseModel):
    def init(self, full_name, age, id=None):
        super().init(full_name, age)
        self.__id = id
    
    @property
    def id(self):
        return self.__id
    
    def save_to_db(self):
        if self.__id is None:
            cursor = self._connection.cursor()
            cursor.execute(
                "INSERT INTO students (full_name, age) VALUES (?, ?)",
                (self.full_name, self.age)
            )
            self.__id = cursor.lastrowid
            self._connection.commit()
        else:
            cursor = self._connection.cursor()
            cursor.execute(
                "UPDATE students SET full_name = ?, age = ? WHERE id = ?",
                (self.full_name, self.age, self.__id)
            )
            self._connection.commit()
    
    def info(self):
        return f"Студент: {self.full_name}, Возраст: {self.age}, ID: {self.id}"
    
    def enroll(self, course):
        enrollment = Enrollment(self.id, course.id)
        enrollment.save_to_db()
        return enrollment
    
    def get_courses(self):
        cursor = self._connection.cursor()
        cursor.execute("""
            SELECT c.id, c.title, c.teacher, e.grade 
            FROM courses c
            JOIN enrollments e ON c.id = e.course_id
            WHERE e.student_id = ?
        """, (self.id,))
        return cursor.fetchall()
    
    @classmethod
    def get_all(cls):
        cursor = cls._connection.cursor()
        cursor.execute("SELECT id, full_name, age FROM students")
        return [Student(row[1], row[2], row[0]) for row in cursor.fetchall()]
    
    @classmethod
    def get_by_id(cls, student_id):
        cursor = cls._connection.cursor()
        cursor.execute("SELECT id, full_name, age FROM students WHERE id = ?", (student_id,))
        row = cursor.fetchone()
        if row:
            return Student(row[1], row[2], row[0])
        return None

class Course(DatabaseModel):
    def init(self, title, teacher, id=None):
        self.__id = id
        self.__title = title
        self.__teacher = teacher
    
    @property
    def id(self):
        return self.__id
    
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, value):
        self.__title = value
    
    @property
    def teacher(self):
        return self.__teacher
    
    @teacher.setter
    def teacher(self, value):
        self.__teacher = value
    
    def save_to_db(self):
        if self.__id is None:
            cursor = self._connection.cursor()
            cursor.execute(
                "INSERT INTO courses (title, teacher) VALUES (?, ?)",
                (self.title, self.teacher)
            )
            self.__id = cursor.lastrowid
            self._connection.commit()
        else:
            cursor = self._connection.cursor()
            cursor.execute(
                "UPDATE courses SET title = ?, teacher = ? WHERE id = ?",
                (self.title, self.teacher, self.__id)
            )
            self._connection.commit()
    
    def info(self):
        return f"Курс: {self.title}, Преподаватель: {self.teacher}, ID: {self.id}"
    
    def get_students(self):
        cursor = self._connection.cursor()
        cursor.execute("""
            SELECT s.id, s.full_name, s.age, e.grade 
            FROM students s
            JOIN enrollments e ON s.id = e.student_id
            WHERE e.course_id = ?
        """, (self.id,))
        return cursor.fetchall()
    
    @classmethod
    def get_all(cls):
        cursor = cls._connection.cursor()
        cursor.execute("SELECT id, title, teacher FROM courses")
        return [Course(row[1], row[2], row[0]) for row in cursor.fetchall()]
    
    @classmethod
    def get_by_id(cls, course_id):
        cursor = cls._connection.cursor()
        cursor.execute("SELECT id, title, teacher FROM courses WHERE id = ?", (course_id,))
        row = cursor.fetchone()
        if row:
            return Course(row[1], row[2], row[0])
        return None

class Enrollment(DatabaseModel):
    def init(self, student_id, course_id, grade=None, id=None):
        self.__id = id
        self.__student_id = student_id
        self.__course_id = course_id
        self.__grade = grade
    
    @property
    def id(self):
        return self.__id
    
    @property
    def student_id(self):
        return self.__student_id
    
    @property
    def course_id(self):
        return self.__course_id
    
    @property
    def grade(self):
        return self.__grade
    
    @grade.setter
    def grade(self, value):
        self.__grade = value
    
    def save_to_db(self):
        if self.__id is None:
            cursor = self._connection.cursor()
            cursor.execute(
                "INSERT INTO enrollments (student_id, course_id, grade) VALUES (?, ?, ?)",
                (self.student_id, self.course_id, self.grade)
            )
            self.__id = cursor.lastrowid
            self._connection.commit()
        else:
            cursor = self._connection.cursor()
            cursor.execute(
                "UPDATE enrollments SET student_id = ?, course_id = ?, grade = ? WHERE id = ?",
                (self.student_id, self.course_id, self.grade, self.__id)
            )
            self._connection.commit()
    
    def info(self):
        return f"Запись: ID студента: {self.student_id}, ID курса: {self.course_id}, Оценка: {self.grade if self.grade else 'не указана'}"
    
    @classmethod
    def get_by_student_and_course(cls, student_id, course_id):
        cursor = cls._connection.cursor()
        cursor.execute("""
            SELECT id, student_id, course_id, grade 
            FROM enrollments 
            WHERE student_id = ? AND course_id = ?
        """, (student_id, course_id))
        row = cursor.fetchone()
        if row:
            return Enrollment(row[1], row[2], row[3], row[0])
        return None
    
    @classmethod
    def get_all(cls):
        cursor = cls._connection.cursor()
        cursor.execute("SELECT id, student_id, course_id, grade FROM enrollments")
        return [Enrollment(row[1], row[2], row[3], row[0]) for row in cursor.fetchall()]

class UniversityApp:
    @staticmethod
    def initialize_database():
        connection = sqlite3.connect('university.db')
        cursor = connection.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT NOT NULL,
                age INTEGER NOT NULL
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                teacher TEXT NOT NULL
            )
        """)
