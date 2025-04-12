import sqlite3

class Library:
    def __init__(self,db_name="books.db"):
        self.connection=sqlite3.connect(db_name)
        self.cursor=self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS books(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL
        )
    """)
        
    def add_book(self,book):
        self.cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)",(book.
        title, book.author))
        self.connection.commit()

    def get_book(self,id):
        self.cursor.execute("SELECT * FROM books WHERE id = ?", (id,))
        return self.cursor.fetchone()
    
    def get_all_books(self):
        self.cursor.execute("SELECT * FROM books")
        return self.cursor.fetchall()
    
    def delete_book_by_id(self,id):
        self.cursor.execute("DELETE FROM books WHERE id = ?",(id,))
        self.connection.commit()
        print(f"The book with id {id} was deleted")


class Book:
    def __init__(self,title,author,id=None):
        self.id=id
        self.title=title
        self.author=author

    
class BookService:
    def __init__(self):
        self.db=Library()

    def add_book(self,book):
        if self.find_book_by_id(book.id):
            print("The book with that id already exists")
            return
        self.db.add_book(book)
        print("The book added succesfully")

    def find_book_by_id(self,id):   
        book_data=self.db.get_book(id)
        if book_data:
            return Book(id=book_data[0],title=book_data[1],author=book_data[2])
        else:
            print("The book is not found")

    def list_of_all_books(self):
        books_data=self.db.get_all_books()
        if books_data:
            for book in books_data:
                print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}")
        else:
            print("There is no book")

    def delete_book_by_id(self,id):
        delete_book=self.find_book_by_id(id)
        if delete_book:
            self.db.delete_book_by_id(id)
        else:
            None
    



service=BookService()


# book1=Book(title='Evgeniy Onegin',author='A.S.Pushkin')
# service.add_book(book1)

# book2=Book(title='Python 101',author='Mike')
# service.add_book(book2)

# book3=Book(title='Human Anatomy',author='Kaplan')
# service.add_book(book3)


# found=service.find_book_by_id(1)
# if found:
#     print(f"Book is found: {found.id}, {found.title}, {found.author}")

# service.list_of_all_books()


# service.delete_book_by_id(1)