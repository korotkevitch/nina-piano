# Generated by Django 4.0.4 on 2022-04-21 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piano', '0004_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='icon',
            field=models.FileField(blank=True, default='', upload_to='', verbose_name='Иконка'),
        ),
    ]