# Book My PG - A PG recommendation application

An app which searches nearby pg and recommend it to the College going students 

# Technology Used 

Django, tailwind, javaScript, Python and more... 

Read more about Django here - link

# Using virtual environment 

Installing every packages in the virtual environment so that it doesn't effect any other project in the system
using cmd - pipenv shell to activate the environment and pipenv instead of pip

Know more about virtual Environment - link

# Dividing whole project into different small apps 

To make our developement a little bit easy we are making different apps for different features 
Here we have apps like :
- Booking
- Conversations
- Rooms 
- Users
- Reviews 
- Lists

# Making the database 

Making database tables for every apps and then populating it with some data.
In django we call it as defining models ( which can be done coding in python language )

# Admin panel

Admin panel is available for the superuser to  create, read, update and delete the data.


** Bonus point - If a function called inside the class it is called METHOD else if outside the class it's function **

# seeding in django
- using django seed to create fake data

 for eg: seeding of facilities in database

 ```python
from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):
    help = 'This command creates facilities'

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
```

# Paginator is awesome 

- from django.core.paginator import Paginator

way to use them :

```python
    def all_rooms(request):
        page = request.GET.get("page")
        room_list = models.Room.objects.all()
        paginator = Paginator(room_list, 10, orphans=5)
        rooms = paginator.get_page(page)
        # print(vars(rooms))
        return render(
            request,
            "rooms/home.html",
            {
                "page": rooms,
            },
        )
```

Here Orphan will help in moving remaining pages to the previous page ( how coool is that ), in this case it will move 5 or less items to previous page

# Exception handeling 
```python
    try:
        rooms = paginator.page(int(page))
        return render(
            request,
            "rooms/home.html",
            {
                "page": rooms,
            },
        )
    except EmptyPage:
        rooms = paginator.page(1)
        return redirect("/")
```