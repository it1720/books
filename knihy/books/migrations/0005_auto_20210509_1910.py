# Generated by Django 3.2.2 on 2021-05-09 17:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_kniha_hodnoceni'),
    ]

    operations = [
        migrations.AddField(
            model_name='kniha',
            name='cena',
            field=models.FloatField(help_text='Zadejte cenu knihy', null=True, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Cena'),
        ),
        migrations.AlterField(
            model_name='kniha',
            name='hodnoceni',
            field=models.IntegerField(blank=True, choices=[(5, 'Výborná'), (4, 'Zabaví'), (3, 'Průměrná'), (2, 'Špatná'), (1, 'Velmi špatná')], default=3, help_text='Vyberte hodnocení knihy', verbose_name='Hodnocení'),
        ),
    ]
