from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):
    help = 'This command creates amenities'
    # print("hello 47")

    # def add_arguments(self, parser):
    #     parser.add_argument(
    #         "--times",
    #         help="how many times I need to tell you?",
    #     )

    def handle(self, *args, **options):

        amenities = [
            "washer",
            "dryer",
            "Air conditioning",
            "Pets allowed",
            "Furnished apartments",
            "Dishwasher",
            "Washer",
            "dryer connections",
            "Some utilities included",
            "Balcony",
            "wifi",
            "geyser",
            "Cable ready",
            "TV",
            "Sofa",
        ]
        # Amenity.objects.create()
        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS(f"{len(amenities)} Amenities created!"))