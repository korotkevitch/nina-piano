# Generated by Django 4.0.4 on 2022-04-21 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piano', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=120, verbose_name='Заголовок')),
                ('text', models.CharField(blank=True, max_length=150, verbose_name='Текст')),
            ],
            options={
                'verbose_name': '       Инфо',
                'verbose_name_plural': '       Инфо',
            },
        ),
    ]