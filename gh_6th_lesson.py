'''GitHub'''

'''
открываем git bash здесь в терминале
вводим:
$ git config --global user.name "John Doe"
$ git config --global user.email johndoe@example.com
'''

'''
в обычном терминале:

git init — Инициализирует новый локальный репозиторий Git в текущей директории. После выполнения этой команды в папке появится скрытая директория .git, в которой будет храниться информация о репозитории.

git add . — Добавляет все изменения (новые файлы, изменения в существующих файлах и удаленные файлы) в индекс (стейджинг). Точка (.) указывает на добавление всех файлов и папок, находящихся в текущей директории.

git commit -m "firs commit" — Создает новый коммит с описанием "firs commit". Ключ -m используется для указания сообщения коммита напрямую в командной строке, в данном случае опечатка в слове "firs" (правильно "first").

git branch -m main — Переименовывает текущую ветку в main. По умолчанию первая ветка называется master, но командой -m (move) можно переименовать её в main.

git remote add origin <<ссылка на ваш репозиторий>> — Добавляет удаленный репозиторий с именем origin. Указываем ссылку на ваш репозиторий (например, на GitHub или другой сервис). После этого команда Git будет знать, куда отправлять изменения при выполнении команд push и pull.

git push -u origin main — Отправляет текущую ветку main в удаленный репозиторий origin и устанавливает отслеживание (tracking) для этой ветки. Ключ -u позволяет связать локальную ветку с удаленной, чтобы в дальнейшем можно было использовать просто git push без указания ветки.
'''