from django.core.management.base import BaseCommand
from faker import Faker 
from fintech.models import Teacher, Group
fake_data = Faker("uz_UZ")
class Command(BaseCommand):

    def handle(self, *args, **options):
        
        print("Group lar yaratilmoqda...")
        for _ in range(100):
            teacher = Teacher.objects.all().order_by("?").first()
            Group.objects.create(
                name = fake_data.word(),
                teacher = teacher
            )
        # oq rand, yashil, qizil
        self.stdout.write(self.style.SUCCESS("100 ta group yaratildi!"))

