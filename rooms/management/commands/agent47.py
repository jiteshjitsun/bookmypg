from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'This command tells me that she loves me'
    # print("hello 47")

    def add_arguments(self, parser):
        parser.add_argument(
            "--times",
            help="how many times I need to tell you?",
        )
    
    def handle(self, *args, **options):
        times = options.get("times")
        for time in range(0, int(times)):
            self.stdout.write(self.style.SUCCESS("I love you"))