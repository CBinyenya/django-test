from django.db import models


class AndelaEngineer(models.Model):
    name = models.CharField(max_length=20)
    level = models.PositiveSmallIntegerField(default=1)

    class Meta:
        db_table = 'engineer'


class PartnerEngineer(models.Model):
    engineer = models.ForeignKey(AndelaEngineer, on_delete=models.CASCADE)
    level = models.PositiveSmallIntegerField(default=1)

    class Meta:
        db_table = 'partner'
