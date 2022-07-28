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
# Запускаем скрипты в Django

#### Для начала вам нужно [создать](https://itproger.com/course/django/2) проект и [создать](https://itproger.com/course/django/3) приложение с выбранным вам названием.
> Советуется называть приложение отталкиваясь от названия вашего проекта

#### Теперь заходим в наше приложения и создаём папки в таком порядке и расположении:

>management
>>commands
>>>scripts.py

#### В __scripts.py__ прописываем следующий код:

```python

import sqlite3
from django.core.management.base import BaseCommand
from pprint import pprint


class Command(BaseCommand):
    help = "Пробегаемся по моделям" # Обязательно пропишите эту переменную, чтобы после ввожа -h было понятно о чём ваш скрипт

    def handle(self, *args, **options):
        with sqlite3.connect("db.sqlite3") as data:
            cursor = data.cursor()
            cursor.execute("""select * from notes_todo""")
            pprint(cursor.fetchall())
        
```
>В примере выше скрипт проходится по основным моделям в базе данных
>В handle прописываете основные функции вашего скрипта

## Запуск скрипта
**Теперь вы можете запускать скрипт прямиком с Django следующей командой**
```python
python3 manage.py scripts
```
___
# API Сайта
**Про создания api вы можете прочитать в форумах в [гугле](https://google.com), здесь я в кратце покажу, что прописывать. :pen:**

#### В urls.py основного проекта в списке urlpatterns добавляем следующий код:
```python
path('testapi/', include('<название приложения>.urls')),
```
>Мы создали страницу testapi к которой будут прикрепляться страницы с __<Названия приложения>.urls__
#### создаём три файла в папке приложения
```python
serializers.py, urls.py, api.py 
```






