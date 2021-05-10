# Generated by Django 3.2.2 on 2021-05-09 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20210509_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kniha',
            name='hodnoceni',
            field=models.IntegerField(blank=True, choices=[(5, 'Výborná'), (4, 'Dobrá'), (3, 'Průměrná'), (2, 'Špatná'), (1, 'Velmi špatná')], default=3, help_text='Vyberte hodnocení knihy', verbose_name='Hodnocení'),
        ),
    ]
