# Generated by Django 3.2.8 on 2021-12-11 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20211206_1513'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('phone', models.CharField(max_length=11, verbose_name='Телефон')),
                ('unikID', models.TextField(verbose_name='Уникальный ID')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время отправки')),
            ],
            options={
                'verbose_name': 'Клиенты',
                'verbose_name_plural': 'Клиенты',
                'ordering': ['-time_create', 'unikID'],
            },
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]