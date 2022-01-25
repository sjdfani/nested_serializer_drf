from django.db import models
from django.contrib.auth.models import User


class AddressManage(models.Manager):
    def all(self):
        return self.filter(state=True)


class Address(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='addresses')
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    address_line = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.BooleanField(default=False)

    objects = AddressManage()

    class Meta:
        verbose_name = 'Addres'

    def __str__(self):
        return self.city