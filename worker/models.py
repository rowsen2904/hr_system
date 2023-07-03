from django.db import models
from django.utils.translation import gettext as _

from branch.models import Branch, Department


class Worker(models.Model):
    class Genders(models.TextChoices):
        MALE = "m", _("Male")
        FEMALE = "f", _("Female")

    
    class Statuses(models.TextChoices):
        ACTIVE = "active", _("Active")
        DELETED = "deleted", _("Deleted")

    branch = models.ForeignKey(
        Branch,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='workers'
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='workers'
    )

    fullname = models.CharField(max_length=255)
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=8)
    emp_number = models.CharField(max_length=30)
    working_since = models.DateField()
    address = models.CharField(max_length=100)
    mail = models.EmailField(max_length=30, null=True, blank=True)
    gender = models.CharField(max_length=15, choices=Genders.choices)
    status = models.CharField(max_length=30, choices=Statuses.choices, default=Statuses.ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)

    photo = models.ImageField(
        upload_to='workers_photo/', null=True, blank=True)
    three_gen = models.FileField(
        upload_to='workers_three_gen/', null=True, blank=True)
    employment_history = models.FileField(
        upload_to='workers_employment_history/', null=True, blank=True)
    passport_copy = models.FileField(
        upload_to='workers_passport_copy/', null=True, blank=True)

    def __str__(self):
        return self.fullname + '(' + self.branch.name + ')'

    @property
    def is_active(self):
        return self.status == self.Statuses.ACTIVE

    @property
    def is_deleted(self):
        return self.status == self.Statuses.DELETED
    
    @property
    def is_male(self):
        return self.gender == self.Genders.MALE

    @property
    def is_female(self):
        return self.gender == self.Genders.FEMALE

    def set_as_deleted(self):
        self.status = self.Statuses.DELETED
        self.save()
