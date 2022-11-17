# Generated by Django 4.1.3 on 2022-11-17 02:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='address',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='room',
            name='baths',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='room',
            name='beds',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='room',
            name='city',
            field=models.CharField(default='', max_length=80),
        ),
        migrations.AddField(
            model_name='room',
            name='country',
            field=django_countries.fields.CountryField(default='india', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='instant_book',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='room',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='room',
            name='owner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='persons',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='room',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]