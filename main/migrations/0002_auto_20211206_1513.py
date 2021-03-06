# Generated by Django 3.2.8 on 2021-12-06 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('message', models.TextField(max_length=1000)),
            ],
        ),
        migrations.AlterModelOptions(
            name='blanks',
            options={'ordering': ['-time_create', 'phone'], 'verbose_name': 'Обратная связь', 'verbose_name_plural': 'Обратная связь'},
        ),
        migrations.AlterField(
            model_name='blanks',
            name='description',
            field=models.TextField(blank=True, verbose_name='Пожелания'),
        ),
        migrations.AlterField(
            model_name='blanks',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='blanks',
            name='phone',
            field=models.CharField(max_length=11, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='blanks',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время отправки'),
        ),
    ]
