# Generated by Django 4.1.3 on 2022-11-25 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]