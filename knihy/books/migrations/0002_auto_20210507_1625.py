# Generated by Django 3.2.2 on 2021-05-07 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kategorie',
            options={'ordering': ['typ'], 'verbose_name': 'Kategorie', 'verbose_name_plural': 'Kategorie'},
        ),
        migrations.AlterModelOptions(
            name='kniha',
            options={'ordering': ['nazev', '-rok'], 'verbose_name': 'Kniha', 'verbose_name_plural': 'Knihy'},
        ),
    ]