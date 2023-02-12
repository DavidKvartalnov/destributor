from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser, models.Model):
    name = models.CharField(max_length=16)
    surname = models.CharField(max_length=32)
    patronymic = models.CharField(max_length=16)
    age = models.PositiveIntegerField(null=True)
    roles = models.ManyToManyField("Role")
    bio = models.TextField()

    groups = None
    first_name = None
    last_name = None

    def __str__(self):
        return f'{self.name} {self.surname}'


class Role(models.Model):
    name = models.CharField(max_length=127)
    description = models.TextField()

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=127)
    cost = models.IntegerField()
    durations = models.DurationField(null=True, default=0)

    def __str__(self):
        return self.name


class SectionKind(models.Model):
    name = models.CharField(max_length=127)

    def __str__(self):
        return self.name


class Section(models.Model):
    name = models.CharField(max_length=127)
    trainer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    section_kind = models.ForeignKey(SectionKind, on_delete=models.SET_NULL, null=True, related_name='section')
    service = models.ManyToManyField(Service)

    def __str__(self):
        return self.name


class SectionGroup(models.Model):
    name = models.CharField(max_length=127)
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True, related_name='group')
    customer = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class Access(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    start_datetime = models.DateTimeField(auto_now=True)
    creation_datetime = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=None, null=True)
    is_subscribe = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()

