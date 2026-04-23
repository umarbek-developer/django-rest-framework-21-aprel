from django.core.management.base import BaseCommand
from faker import Faker 
from aprel23.models import Category, Product 
from random import randint

fake_data = Faker("uz_UZ")
class Command(BaseCommand):

    def handle(self, *args, **options):
        
        print("Category lar yaratilmoqda...")
        for _ in range(100):
            Category.objects.create(
                title = fake_data.word(),
                is_active = True if randint(0,1) else False,
            )
        # oq rand, yashil, qizil
        self.stdout.write(self.style.SUCCESS("100 ta category yaratildi!"))

