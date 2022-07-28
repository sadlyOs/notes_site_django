# notes_site_django
### Notes_site Django :laughing:
___
**Notes_site** - Это сайт с заметками написанный на __html/css/js/python(Django)__, в котором пользователи могут регестрироваться, оставлять заметки и их выполнять.


**Notes_site api** - Сайт имеет свою api, написана на библиотеке __djangorestframework__, ниже будет расмотрено её создание

**Запуск других различных скриптов** - В проекте по мимо тестового сервера можно будет запускать и другие скрипты, ниже тоже будет это расмотрено

## :gear: Установка
**Клонируем репозиторий:**
```python
https://github.com/sadlyOs/notes_site_django.git
```
**Устанавливаем виртуальное окружение следующей командой**
```python
python3 -m env venv
```

**Устанавливаем все нужные библиотеки из файла requirements.txt**
```python
python3 -m pip3 install -r requirements.txt 
```

> **Запускаем наш тестовый сервер**

**Запуск на Windows:**
```python
python manage.py runserver
```
   
**Запуск на Linux**
```python
python3 manage.py runserver
```
___

# Запускаем скриптов в Django
