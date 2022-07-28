from django.core.management.base import BaseCommand
from notes.models import Todo
from jinja2 import Template
import sqlite3
from pprint import pprint

data = sqlite3.connect("db.sqlite3")


class Command(BaseCommand):
    help = "Телеграм-бот"

    def handle(self, *args, **options):
        cursor = data.cursor()
        cursor.execute("""select * from notes_todo""")
        pprint(cursor.fetchall())
