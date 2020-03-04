from django.db import models


class Latest(models.Model):
    latest = models.CharField(max_length=150)

    def __str__(self):
        print(self.latest)

