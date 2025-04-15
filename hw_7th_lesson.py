import sqlite3
from dataclasses import dataclass

@dataclass
class Task:
    id: int = None
    title: str = ""
    description: str = ""
    is_done: bool = False

    def save(self):
        conn = sqlite3.connect('todo.db')
        cursor = conn.cursor()
        
        if self.id is None:
            cursor.execute('''
                INSERT INTO tasks (title, description, is_done)
                VALUES (?, ?, ?)
            ''', (self.title, self.description, self.is_done))
        else:
            cursor.execute('''
                UPDATE tasks
                SET title = ?, description = ?, is_done = ?
                WHERE id = ?
            ''', (self.title, self.description, self.is_done, self.id))
        
        conn.commit()
        if self.id is None:
            self.id = cursor.lastrowid
        conn.close()

    def mark_done(self):
        self.is_done = True
        self.save()

    def delete(self):
        if self.id is not None:
            conn = sqlite3.connect('todo.db')
            cursor = conn.cursor()
            cursor.execute('DELETE FROM tasks WHERE id = ?', (self.id,))
            conn.commit()
            conn.close()

class TaskManager:
    @staticmethod
    def create_table():
        conn = sqlite3.connect('todo.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                is_done BOOLEAN DEFAULT FALSE
            )
        ''')
        conn.commit()
        conn.close()

    @staticmethod
    def get_all_tasks():
        conn = sqlite3.connect('todo.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, title, description, is_done FROM tasks')
        tasks = []
        for row in cursor.fetchall():
            task = Task(id=row[0], title=row[1], description=row[2], is_done=row[3])
            tasks.append(task)
        conn.close()
        return tasks

    @staticmethod
    def get_pending_tasks():
        conn = sqlite3.connect('todo.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, title, description, is_done FROM tasks WHERE is_done = FALSE')
        tasks = []
        for row in cursor.fetchall():
            task = Task(id=row[0], title=row[1], description=row[2], is_done=row[3])
            tasks.append(task)
        conn.close()
        return tasks

    @staticmethod
    def get_task_by_id(task_id):
        conn = sqlite3.connect('todo.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, title, description, is_done FROM tasks WHERE id = ?', (task_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Task(id=row[0], title=row[1], description=row[2], is_done=row[3])
        return None

    @staticmethod
    def delete_task(task_id):
        conn = sqlite3.connect('todo.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        conn.commit()
        conn.close()

def display_menu():
    print("\nМенеджер задач")
    print("1. Показать все задачи")
    print("2. Показать невыполненные задачи")
    print("3. Добавить задачу")
    print("4. Отметить задачу как выполненную")
    print("5. Удалить задачу")
    print("0. Выход")

def main():
    TaskManager.create_table()
    
    while True:
        display_menu()
        choice = input("Выберите действие: ")
        
        if choice == "1":
            tasks = TaskManager.get_all_tasks()
            print("\nВсе задачи:")
            for task in tasks:
                status = "✓" if task.is_done else "✗"
                print(f"{task.id}. [{status}] {task.title} - {task.description}")
        
        elif choice == "2":
            tasks = TaskManager.get_pending_tasks()
            print("\nНевыполненные задачи:")
            for task in tasks:
                print(f"{task.id}. {task.title} - {task.description}")
        
        elif choice == "3":
            title = input("Введите название задачи: ")
            description = input("Введите описание задачи: ")
            new_task = Task(title=title, description=description)
            new_task.save()
            print("Задача успешно добавлена!")
        
        elif choice == "4":
            task_id = int(input("Введите ID задачи для отметки как выполненной: "))
            task = TaskManager.get_task_by_id(task_id)
            if task:
                task.mark_done()
                print("Задача отмечена как выполненная!")
            else:
                print("Задача с таким ID не найдена.")
        
        elif choice == "5":
            task_id = int(input("Введите ID задачи для удаления: "))
            task = TaskManager.get_task_by_id(task_id)
            if task:
                task.delete()
                print("Задача успешно удалена!")
            else:
                print("Задача с таким ID не найдена.")
        
        elif choice == "0":
            print("Выход из программы.")
            break
        
        else:
            print("Неверный ввод. Пожалуйста, выберите действие из меню.")

if __name__ == "__main__":
    main()