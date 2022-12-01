from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):
    help = 'This command creates facilities'
    # print("hello 47")

    # def add_arguments(self, parser):
    #     parser.add_argument(
    #         "--times",
    #         help="how many times I need to tell you?",
    #     )

    def handle(self, *args, **options):

        facilities = [
            "private entrance",
            "parking",
            "elevator",
            "gym",
        ]
        # Amenity.objects.create()
        for a in facilities:
            Facility.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} facilities created!"))