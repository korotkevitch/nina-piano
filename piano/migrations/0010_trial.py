# Generated by Django 4.0.4 on 2022-04-22 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piano', '0009_remove_task_bg_info_bg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=120, verbose_name='Заголовок')),
                ('text', models.CharField(blank=True, max_length=1000, verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Пробный урок',
                'verbose_name_plural': 'Пробный урок',
            },
        ),
    ]
