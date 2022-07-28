from django.core.management.base import BaseCommand
from notes.models import Todo
import sqlite3
from pprint import pprint


class Command(BaseCommand):
    help = "Телеграм-бот"

    def handle(self, *args, **options):
        with sqlite3.connect("db.sqlite3") as data:
            cursor = data.cursor()
            cursor.execute("""select * from notes_todo""")
            pprint(cursor.fetchall())
