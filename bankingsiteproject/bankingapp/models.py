from django.db import models

class District(models.Model):
    name = models.CharField(max_length=100, unique=True)
    wikipedia_link = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Branch(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
