from django.db import models

# Create your models here.


class Recent(models.Model):
    text = models.CharField(max_length=80)
    output = models.TextField()

    def __str__(self):
        return self.text
