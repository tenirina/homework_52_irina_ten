from django.db import models


class ToDo(models.Model):
    text = models.TextField(verbose_name="Description", max_length=500, null=False, blank=False)
    status = models.CharField(verbose_name="Status", max_length=50, null=False, default="New")
    completion_data = models.DateField(verbose_name="Date of completion", null=True, default=None)

    def __str__(self):
        return f"{self.status} - {self.text}"
