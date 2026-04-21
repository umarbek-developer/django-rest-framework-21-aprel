from django.core.management.base import BaseCommand
from faker import Faker 
from fintech.models import Teacher, Group, Student

fake_data = Faker("uz_UZ")
class Command(BaseCommand):

    def handle(self, *args, **options):
        
        print("Group lar yaratilmoqda...")
        for _ in range(100):
            group = Group.objects.all().order_by("?").first()
            Student.objects.create(
                first_name = fake_data.name(),
                last_name = fake_data.last_name(),
                group = group
            )
        # oq rand, yashil, qizil
        self.stdout.write(self.style.SUCCESS("100 ta group yaratildi!"))

