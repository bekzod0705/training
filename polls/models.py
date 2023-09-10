from django.db import models

# Create your models here.

class info(models.Model):
    name=models.CharField(max_length=60,default='')
    surname=models.CharField(max_length=60,default='')
    count=models.PositiveIntegerField(default=1)

    class Meta:
        db_table='msg'
        
    def __str__(self) -> str:
        return self.name
