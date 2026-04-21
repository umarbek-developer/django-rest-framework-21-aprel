from django.core.management.base import BaseCommand
from faker import Faker 
from fintech.models import Teacher
fake_data = Faker("uz_UZ")
class Command(BaseCommand):

    def handle(self, *args, **options):
        
        print("Teacher lar yaratilmoqda...")
        for _ in range(100):
            Teacher.objects.create(
                first_name = fake_data.first_name(),
                last_name = fake_data.last_name(),
                specialization = fake_data.job(),
                email = fake_data.safe_email(),
            )
        # oq rand, yashil, qizil
        self.stdout.write(self.style.SUCCESS("100 ta teacher yaratildi!"))
        self.stdout.write(self.style.ERROR("Xatolik chiqdi"))

