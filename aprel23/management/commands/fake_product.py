from django.core.management.base import BaseCommand
from faker import Faker
from random import randint
from aprel23.models import Category, Product

fake_data = Faker("uz_Uz")

class Command(BaseCommand):

    def handle(self, *args, **options):
        print("productlar yaratilmoqda...")
        categories = Category.objects.all()
        for _ in range(100):
            category = categories.order_by("?").first()
            Product.objects.create(
                title=fake_data.word(),
                category=category,
                price=randint(10000, 99999),
                is_active=True if randint(0,1) else False
            )
        self.stdout.write(self.style.SUCCESS("100 ta product yaratildi."))
