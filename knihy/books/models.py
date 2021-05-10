from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator

# Create your models here.
class kategorie(models.Model):
    typ = models.CharField(max_length=50, unique=True, verbose_name="Název kategorie",
                           help_text='Zadejte podkategorii')
    KATEGORIE = (
        ('Beletrie', 'beletrie'),
        ('Poezie', 'poezie'),
        ('Historická literatura', 'historicka_literatura'),
        ('Literatura pro děti a mládež', 'deti_literatura'),
        ('Odborná literatura', 'odborna_literatura'),
        ('Naučná literatura', 'naucna_literatura'),
        ('Kuchařky', 'kucharky'),
        ('Cestování', 'cestovani'),
        ('Zdraví', 'zdravi'),

    )
    oblast = models.CharField(max_length=50,choices=KATEGORIE, blank=True, default='Beletrie', verbose_name="Kategorie")

    class Meta:
        ordering = ["typ"]
        verbose_name = 'Kategorie'
        verbose_name_plural = 'Kategorie'

    def __str__(self):
        return f"{self.typ}, {self.KATEGORIE}"


class kniha(models.Model):
    nazev = models.CharField(max_length=50, verbose_name="Název knihy")
    autor_jmeno = models.CharField(max_length=50, verbose_name="Jméno autora")
    autor_prijmeni = models.CharField(max_length=50, verbose_name="Příjmení autora")
    rok = models.DateField(auto_now_add=True)
    popis = models.TextField(blank=True, null=True, verbose_name="Popis knihy")
    cena = models.FloatField(validators=[MinValueValidator(0.0)], null=True,
                             help_text="Zadejte cenu knihy", verbose_name="Cena")
    HODNOCENI = (
        (5, 'Výborná'),
        (4, 'Dobrá'),
        (3, 'Průměrná'),
        (2, 'Špatná'),
        (1, 'Velmi špatná'),
    )
    hodnoceni = models.IntegerField(choices=HODNOCENI, blank=True, default=3, verbose_name="Hodnocení",
                                    help_text='Vyberte hodnocení knihy')
    foto = models.ImageField(upload_to='knihy/%Y/%m/%d', blank=True, null=True, verbose_name="Foto knihy")
    kategorie = models.ForeignKey(kategorie, on_delete=models.RESTRICT)

    class Meta:
        ordering = ["-hodnoceni"]
        verbose_name = 'Kniha'
        verbose_name_plural = 'Knihy'

    def __str__(self):
        return f"{self.nazev}"

    def get_absolute_url(self):
        return reverse('detail',args=(str(self.id)))