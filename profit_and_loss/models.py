import os

from django.db import models
from django.utils.deconstruct import deconstructible


@deconstructible
class PathRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # set filename as random string
        filename = '{}.{}'.format('departments', ext)
        # return the whole path to the file
        return os.path.join(self.path, filename)


path_and_rename = PathRename('files/')


# Create your models here.


class Departments(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Customers(models.Model):
    date = models.DateField(null=True, blank=True)
    departments = models.ForeignKey(Departments, related_name='departments', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=30)
    sales = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Result(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)

    # def path_and_rename(path):  # потом добавить аргумент кого во что переименовать соответственно
    #     def wrapper(instance, filename):
    #         ext = filename.split(".")[-1]
    #         # g filename
    #         filename = "{}.{}".format('departments', ext)
    #         # return the whole path to the file
    #         return os.path.join(path, filename)
    #
    #     return wrapper
    file = models.FileField(upload_to=path_and_rename, null=True)

    # file = models.FileField(upload_to=path_and_rename('files/'), null=True)
    # file = models.FileField(upload_to=path_and_rename, verbose_name=(u'departments'), null=True)

    # file = models.FileField(upload_to='files/', null=True)

    def __repr__(self):
        return 'Result(%s, %s)' % (self.name, self.file)

    def __str__(self):
        return self.name


class DepartmentsMonth(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    # name = models.ForeignKey(Departments, max_length=255, on_delete=models.CASCADE)
    buyer_category = models.CharField(max_length=255, blank=False, null=False)
    date = models.DateField(null=True, blank=True, default=None)
    value = models.FloatField(null=True, blank=True, default=None)

    def __str__(self):
        return self.name


class DepartmentsAllData(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    buyer_category = models.CharField(max_length=255, blank=False, null=False)
    product = models.CharField(max_length=255, blank=False, null=False)
    date = models.DateField(null=True, blank=True, default=None)
    sale_value = models.FloatField(null=True, blank=True, default=None)
    cost_price = models.FloatField(null=True, blank=True, default=None)
    quantity = models.FloatField(null=True, blank=True, default=None)
