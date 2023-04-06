from django.db import models


class MoteType(models.IntegerChoices):
    null = 0, 'NullMote'
    water = 1, 'WMote'
    energy = 2, 'EMote'


class Motes(models.Model):
    name = models.CharField(max_length=255)
    type = models.IntegerField(default=MoteType.null, choices=MoteType.choices)
    section = models.CharField(max_length=255, null=False)
    location = models.CharField(max_length=255, null=False)


class Data(models.Model):
    mote = models.ForeignKey(Motes, on_delete=models.CASCADE, default=0)
    last_collection = models.FloatField(
        default=0)  # Litros/Hora no último minuto
    total = models.FloatField(default=0)  # Listros totais
    collect_date = models.DateTimeField(auto_now_add=True)  # Data de coleta
