from django.db import models

class Film(models.Model):
    country = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    year = models.IntegerField(null=True, blank=True)

    def str(self):
        return f'{self.title}'

