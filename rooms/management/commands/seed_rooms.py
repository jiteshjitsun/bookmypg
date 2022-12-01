import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from rooms import models as room_models
from users import models as user_models

class Command(BaseCommand):
    help = "This command creates many rooms"
    # print("hello 47")

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help="how many users you want to create",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        room_types = room_models.RoomType.objects.all()
        print(room_types, all_users)
        seeder.add_entity(room_models.Room, number, {
            "name": lambda x: seeder.faker.address(),
            "owner": lambda x: random.choice(all_users),
            "room_type": lambda x: random.choice(room_types),
            "price": lambda x: random.randint(1, 10000),
            "beds": lambda x: random.randint(1, 5),
            "baths": lambda x: random.randint(1, 5),
            "persons": lambda x: random.randint(1, 10),
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} rooms created!"))