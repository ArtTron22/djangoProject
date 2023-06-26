# Generated by Django 4.2.2 on 2023-06-22 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Ничего интересного', max_length=50, verbose_name='Название')),
                ('anons', models.CharField(default='Никаких анонсов', max_length=250, verbose_name='Анонс')),
                ('full_text', models.TextField(verbose_name='Текст статьи')),
                ('date', models.DateField(verbose_name='Дата публикации')),
            ],
        ),
    ]
