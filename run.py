from main import User, UserService

user=UserService()

# Добавление пользователя

# user_service=User(name='Aslan',email='aslan@gmail.com',age=18)
# user.add_user(user_service)


# Нахождение пользователя

# find=user.find_user_by_email('aslan@gmail.com')
# if find:
#     print(f"Пользователь найден: {find.name}, {find.email}, {find.age}")



# Удаление пользователя

delete = user.delete_user_by_email('aslan@gmail.com')

