from django.db import models


class Count(models.Model):
    name=models.CharField(max_length=10)
    count = models.IntegerField(default=10)

    def __str__(self):
        return self.count

