from django.db import models

class WeightRecord(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    weight = models.FloatField()
    percentage = models.FloatField()

    def __str__(self):
        return f"Record at {self.timestamp}: Weight={self.weight} g, Percentage={self.percentage}%"
