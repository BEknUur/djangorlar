# python modules
import random
from datetime import date

# django modules
from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from django.db import transaction
from django.utils import timezone

# other modules
from faker import Faker

# project modules
from apps.users.models import CustomUser

DEPARTMENTS = ["IT", "HR", "Sales", "Finance"]
ROLES = ["admin", "manager", "employee"]


class Command(BaseCommand):
    help = "Generate users with Faker using bulk_create in batches"

    def add_arguments(self, parser):
        parser.add_argument(
            "--count",
            type=int,
            default=10000,
            help="How many users to create (default: 10000)",
        )
        parser.add_argument(
            "--batch",
            type=int,
            default=1000,
            help="Batch size for bulk_create (default: 1000)",
        )

    def handle(self, *args, **options):
        count = options["count"]
        batch_size = options["batch"]

        fake = Faker()
        Faker.seed(42)
        random.seed(42)

        password_hash = make_password("12345")
        self.stdout.write(
            self.style.NOTICE(f"Generating {count} users in batches of {batch_size}...")
        )

        users = []
        created = 0
        start_birth = date(1975, 1, 1)
        end_birth = date(2005, 12, 31)
        tz = timezone.get_current_timezone()

        for i in range(count):
            email = fake.unique.email()
            birth = (
                fake.date_between_dates(start_birth, end_birth)
                if random.random() > 0.05
                else None
            )

            user = CustomUser(
                email=email,
                fullname=f"{fake.first_name()}_{fake.last_name()}_{i}",
                username=fake.unique.user_name(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                phone=fake.phone_number(),
                city=fake.city(),
                country=fake.country(),
                department=random.choice(DEPARTMENTS),
                role=random.choice(ROLES),
                birth_date=birth,
                salary=random.randint(150_000, 1_000_000),
                is_active=True,
                is_staff=False,
                is_superuser=False,
                date_joined=fake.date_time_between(
                    start_date="-3y", end_date="now", tzinfo=tz
                ),
                password=password_hash,
            )
            users.append(user)

            if len(users) >= batch_size:
                with transaction.atomic():
                    CustomUser.objects.bulk_create(users, batch_size=batch_size)
                created += len(users)
                self.stdout.write(f"Inserted: {created}")
                users.clear()

        if users:
            with transaction.atomic():
                CustomUser.objects.bulk_create(users, batch_size=batch_size)
            created += len(users)

        self.stdout.write(self.style.SUCCESS(f"Done. Total created: {created}"))
