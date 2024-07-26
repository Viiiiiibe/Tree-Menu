# Tree-Menu
### Тестовое задание. Древовидное меню, выводимое через template tag и реализованное с использованием только Django и стандартной библиотеки Python.



## Запуск проекта
- В основной папке установить и активировать виртуальное окружение
```console  
python -m venv venv
```
```console  
.\venv\Scripts\activate.bat
```

- Установить используемые библиотеки из файла requirements.txt
```console  
pip install -r requirements.txt
``` 
- В папке с файлом manage.py выполнить команду для миграций:
```console  
python manage.py migrate
```
- В папке с файлом manage.py создать суперпользователя:
```console  
python manage.py createsuperuser
```
- В папке с файлом manage.py выполнить команду для запуска локального сервера:
```console  
python manage.py runserver
```
- Создать в админке меню main_menu и его пункты
http://127.0.0.1:8000/admin/
- Меню отобразится по адресу
http://127.0.0.1:8000/
- Для отрисовки других меню добавить в index.html тег {% draw_menu 'имя_меню' %}