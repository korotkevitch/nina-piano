# Generated by Django 4.0.4 on 2022-04-23 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piano', '0012_testimonial_alter_stuff_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(blank=True, max_length=50, verbose_name='Имя')),
                ('l_name', models.CharField(blank=True, max_length=50, verbose_name='Фамилия')),
                ('age', models.CharField(blank=True, max_length=50, verbose_name='Возраст')),
                ('phone', models.CharField(blank=True, max_length=50, verbose_name='Телефон')),
                ('message', models.TextField(blank=True, max_length=500, verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Сообщение, заказ',
                'verbose_name_plural': 'Сообщения, заказы',
            },
        ),
    ]
