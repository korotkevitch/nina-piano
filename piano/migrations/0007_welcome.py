# Generated by Django 4.0.4 on 2022-04-22 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piano', '0006_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='Welcome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=120, verbose_name='Заголовок')),
                ('text', models.CharField(blank=True, max_length=150, verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Добро пожаловать',
                'verbose_name_plural': 'Добро пожаловать',
            },
        ),
    ]
