'''
Система управления студентами и курсами
📌 Цель:
Создать консольное приложение для учета студентов, курсов и их записей на курсы с использованием ООП и SQLite3.

🧱 Таблицы в базе данных (SQLite3):
students(id, full_name, age)
courses(id, title, teacher)
enrollments(id, student_id, course_id, grade)
💡 Требования по ООП:
✅ 1. Инкапсуляция:
Все важные данные (__id, __connection, __name) сделать приватными.
Доступ к данным — только через get_, set_.
✅ 2. Наследование:
Базовый класс Person, от которого наследуется Student.
Базовый класс DatabaseModel, от которого наследуются Student, Course, Enrollment.
✅ 3. Полиморфизм:
Метод info() должен работать по-разному в Student, Course, Enrollment.
Метод save_to_db() должен быть переопределён в разных моделях.
✅ 4. Абстракция:
Все SQL-запросы должны быть "спрятаны" внутри методов.
Пользователь работает с понятным интерфейсом: student.enroll(course) — а не cursor.execute(...)
🧪 Функциональность:
 Добавить студента
 Добавить курс
 Записать студента на курс
 Присвоить оценку
 Посмотреть список студентов и их курсов
 Посмотреть курсы и кто на них записан
📘 Пример CLI меню:
1. Добавить студента
2. Добавить курс
3. Записать на курс
4. Поставить оценку
5. Показать студентов и курсы
6. Показать курсы и студентов
7. Выход
'''



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
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS enrollments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER NOT NULL,
                course_id INTEGER NOT NULL,
                grade INTEGER,
                FOREIGN KEY (student_id) REFERENCES students(id),
                FOREIGN KEY (course_id) REFERENCES courses(id),
                UNIQUE(student_id, course_id)
            )
        """)
        
        connection.commit()
        connection.close()
    
    @staticmethod
    def run():
        DatabaseModel.connect()
        
        while True:
            print("\nМеню:")
            print("1. Добавить студента")
            print("2. Добавить курс")
            print("3. Записать на курс")
            print("4. Поставить оценку")
            print("5. Показать студентов и курсы")
            print("6. Показать курсы и студентов")
            print("7. Выход")
            
            choice = input("Выберите пункт меню: ")
            
            if choice == "1":
                UniversityApp.add_student()
            elif choice == "2":
                UniversityApp.add_course()
            elif choice == "3":
                UniversityApp.enroll_student()
            elif choice == "4":
                UniversityApp.set_grade()
            elif choice == "5":
                UniversityApp.show_students_and_courses()
            elif choice == "6":
                UniversityApp.show_courses_and_students()
            elif choice == "7":
                print("Выход из программы.")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")
        
        DatabaseModel.close()
    
    @staticmethod
    def add_student():
        print("\nДобавление нового студента")
        full_name = input("Введите ФИО студента: ")
        age = int(input("Введите возраст студента: "))
        
        student = Student(full_name, age)
        student.save_to_db()
        print(f"Студент {full_name} успешно добавлен с ID {student.id}")
    
    @staticmethod
    def add_course():
        print("\nДобавление нового курса")
        title = input("Введите название курса: ")
        teacher = input("Введите имя преподавателя: ")
        
        course = Course(title, teacher)
        course.save_to_db()
        print(f"Курс {title} успешно добавлен с ID {course.id}")
    
    @staticmethod
    def enroll_student():
        print("\nЗапись студента на курс")
        
        students = Student.get_all()
        if not students:
            print("Нет доступных студентов. Сначала добавьте студентов.")
            return
        
        print("\nСписок студентов:")
        for student in students:
            print(student.info())
        
        student_id = int(input("Введите ID студента: "))
        student = Student.get_by_id(student_id)
        if not student:
            print("Студент с таким ID не найден.")
            return
        
        courses = Course.get_all()
        if not courses:
            print("Нет доступных курсов. Сначала добавьте курсы.")
            return
        
        print("\nСписок курсов:")
        for course in courses:
            print(course.info())
        
        course_id = int(input("Введите ID курса: "))
        course = Course.get_by_id(course_id)
        if not course:
            print("Курс с таким ID не найден.")
            return
        
        existing_enrollment = Enrollment.get_by_student_and_course(student_id, course_id)
        if existing_enrollment:
            print("Этот студент уже записан на данный курс.")
            return
        
        enrollment = student.enroll(course)
        print(f"Студент {student.full_name} успешно записан на курс {course.title}")
    
    @staticmethod
    def set_grade():
        print("\nУстановка оценки студенту за курс")
        
        students = Student.get_all()
        if not students:
            print("Нет доступных студентов.")
            return
        
        print("\nСписок студентов:")
        for student in students:
            print(student.info())
        
        student_id = int(input("Введите ID студента: "))
        student = Student.get_by_id(student_id)
        if not student:
            print("Студент с таким ID не найден.")
            return
        
        courses = student.get_courses()
        if not courses:
            print("У этого студента нет записей на курсы.")
            return
        
        print("\nКурсы, на которые записан студент:")
        for i, course in enumerate(courses, 1):
            print(f"{i}. {course[1]} (Преподаватель: {course[2]}, Оценка: {course[3] if course[3] else 'нет'})")
        
        course_index = int(input("Введите номер курса для установки оценки: ")) - 1
        if course_index < 0 or course_index >= len(courses):
            print("Неверный выбор курса.")
            return
        
        course_id = courses[course_index][0]
        grade = int(input("Введите оценку (1-5): "))
        if grade < 1 or grade > 5:
            print("Оценка должна быть от 1 до 5.")
            return
        
        enrollment = Enrollment.get_by_student_and_course(student_id, course_id)
        if enrollment:
            enrollment.grade = grade
            enrollment.save_to_db()
            print(f"Оценка {grade} успешно установлена для студента {student.full_name} за курс {courses[course_index][1]}")
        else:
            print("Ошибка: запись на курс не найдена.")
    
    @staticmethod
    def show_students_and_courses():
        print("\nСписок студентов и их курсов:")
        
        students = Student.get_all()
        if not students:
            print("Нет доступных студентов.")
            return
        
        for student in students:
            print(f"\n{student.info()}")
            courses = student.get_courses()
            if courses:
                print("Записан на курсы:")
                for course in courses:
                    print(f"- {course[1]} (Преподаватель: {course[2]}, Оценка: {course[3] if course[3] else 'нет'})")
            else:
                print("Не записан ни на один курс.")
    
    @staticmethod
    def show_courses_and_students():
        print("\nСписок курсов и их студентов:")
        
        courses = Course.get_all()
        if not courses:
            print("Нет доступных курсов.")
            return
        
        for course in courses:
            print(f"\n{course.info()}")
            students = course.get_students()
            if students:
                print("Студенты на курсе:")
                for student in students:
                    print(f"- {student[1]} (Возраст: {student[2]}, Оценка: {student[3] if student[3] else 'нет'})")
            else:
                print("На курс пока никто не записан.")

if name == "main":
    UniversityApp.initialize_database()
    UniversityApp.run()