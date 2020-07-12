from django.db import models

class Pledge(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    amount = models.DecimalField(decimal_places=2, max_digits=100, default=25)

    def __str__(self):
        return self.last_name+", "+self.first_name
