# Generated by Django 4.2 on 2023-04-13 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateField(auto_now_add=True, verbose_name='date published'),
        ),
    ]