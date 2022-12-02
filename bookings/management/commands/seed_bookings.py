from django.core.management.base import BaseCommand
from django_seed import Seed
from datetime import datetime, timedelta
from bookings import models as bookings_models
from lists import models as list_models
from users import models as user_models
from rooms import models as room_models
import random

NAME = "bookings"

class Command(BaseCommand):
    help = f"This command creates {NAME}"
    # print("hello 47")

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help=f"how many {NAME} you want to create",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()
        seeder.add_entity(
            bookings_models.Reservation,
            number,
            {
                "status": lambda x: random.choice(["pending", "confirmed", "cancelled"]),
                "guest": lambda x: random.choice(users),
                "room": lambda x: random.choice(rooms),
                "check_in": lambda x: datetime.now(),
                "check_out": lambda x: datetime.now() + timedelta(days=random.randint(2, 400))
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} created!"))