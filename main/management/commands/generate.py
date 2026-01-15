from random import randint
from django.core.management.base import BaseCommand, CommandError
from django.template.defaultfilters import title

from main.models import University
from faker import Faker

class Command(BaseCommand):
     help = 'Add university to database'

     def add_arguments(self, parser):
         parser.add_argument('total', type=int, help='Кількість університетів для додавання')

     def handle(self, *args, **kwargs):
         total = kwargs['total']
         for i in range(total):
             b = Faker()
             try:
                 University.objects.create(
                     title = b.street_title(),
                     code = randint(1, 9999),
                     ownership = b.ownership,
                     rector = b.rector,
                     location = b.location,
                     phone = b.phone,
                     email = b.email,
                     website = b.website,
                     military_department = b.military_department,
                     grants = b.grants,
                     year = str(b.year)
                 )
             except:
                 raise CommandError('Не вдалося додати університет')
             else:
                 print(f'{i+1} університетів додалося')