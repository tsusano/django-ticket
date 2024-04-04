from django.db import models
from django.db import connections

# Create your models heres


class passengerDetail(models.Model):
    name = models.CharField(db_column="Name", max_length=100)
    age = models.IntegerField(db_column="Age")
    gender = models.CharField(db_column="Gender", max_length=6)
    mobile = models.IntegerField(db_column="Mobile")
    email = models.EmailField(db_column="Email", max_length=30)
    date = models.CharField(db_column="Date", max_length=12)
    source = models.CharField(db_column="Source", max_length=50)
    destination = models.CharField(db_column="Destination", max_length=50)
    imagepath = models.CharField(db_column="ImagePath", max_length=50)

    class Meta:
        db_table = "detail"
