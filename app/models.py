from django.db import models

class StockData(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=25)
    open_price = models.DecimalField(max_digits=10,decimal_places=2)
    high_price = models.DecimalField(max_digits=10,decimal_places=2)
    low_price = models.DecimalField(max_digits=10,decimal_places=2)
    close_price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.name

class updateLogs(models.Model):
    update_date = models.DateTimeField()