from django.db import models



class Lead(models.Model):
    name = models.CharField(max_length=250) 
    mobile_1 = models.CharField(max_length=250)
    mobile_2 = models.CharField(max_length=250)
    address = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name