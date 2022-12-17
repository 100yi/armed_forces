# Generated by Django 4.1.3 on 2022-12-17 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armed_universities', '0002_remove_armed_university_country_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='armed_university',
            options={'ordering': ['id'], 'verbose_name': 'Военный вуз', 'verbose_name_plural': 'Военные вузы'},
        ),
        migrations.AddField(
            model_name='armed_university',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True, verbose_name='URL'),
        ),
    ]
