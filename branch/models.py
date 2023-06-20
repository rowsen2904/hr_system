from django.db import models


class Branch(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Branches"

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=100)
    branch = models.ManyToManyField(Branch, related_name="department")

    def __str__(self):
        return self.name
