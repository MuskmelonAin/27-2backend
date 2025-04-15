import sqlite3

class DataBaseManager:
    def __init__(self,db_name="users.db"):
        self.connection=sqlite3.connect(db_name)
        self.cursor=self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR (20) NOT NULL,
            age INTEGER
        )
    """)
        
    def add_user(self,user):
        self.cursor.execute("INSERT INTO users (name,age) VALUES (?, ?)",(user.
        name, user.age))
        self.connection.commit()

    def get_user(self,id):
        self.cursor.execute("SELECT * FROM users WHERE id = ?", (id,))
        return self.cursor.fetchone()
    
    def delete_user_by_id(self,id):
        self.cursor.execute("DELETE FROM users WHERE id = ?",(id,))
        self.connection.commit()
        print(f"Пользователь с id {id} был удален")



class User:
    def __init__(self,name,age,id=None):
        self.id=id
        self.name=name
        self.age=age

    

class Admin(User):
    def __init__(self):
        self.db = DataBaseManager()

    def add_user(self, user):
        self.db.add_user(user)
        print("Пользователь успешно добавлен")

    def delete_user_by_id(self, id):
        user_to_delete = self.find_user_by_id(id)
        if user_to_delete:
            self.db.delete_user_by_id(id)

            
class Customer(User):
    def find_user_by_id(self, id):   
        user_data = self.db.get_user(id)
        if user_data:
            return User(id=user_data[0], name=user_data[1], age=user_data[2])
        else:
            print("Пользователь не найден")

service=Admin()



user1=User(name='Ain',age=18)
service.add_user(user1)


# find=Customer.find_user_by_id(1)
# if find:
#     print(f"Пользователь найден: {find.name}, {find.age}")





# delete = service.delete_user_by_id(1)

