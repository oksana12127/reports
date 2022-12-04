import os

from django.db import models


from uuid import uuid4

# Create your models here.


# def path_and_rename(path):  # потом добавить аргумент кого во что переименовать соответственно
#         def wrapper(instance, filename):
#             ext = filename.split(".")[-1]
#             # g filename
#             filename = "{}.{}".format('departments', ext)
#             # return the whole path to the file
#             return os.path.join(path, filename)
#
#         return wrapper


# def path_and_rename(instance, filename):
#     ext = filename.split('.')[-1]
#     filename_start = filename.replace('.' + ext, '')
#
#     filename = "%s.%s" % (filename_start, ext)
#     return os.path.join('files', filename)


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


# class AllSales(models.Model):
#     # email = models.EmailField()
#     name = models.CharField(max_length=255, blank=False, null=False)
#
#
#
#     # def path_and_rename(path):  # потом добавить аргумент кого во что переименовать соответственно
#     #     def wrapper(instance, filename):
#     #         ext = filename.split(".")[-1]
#     #         # get filename
#     #         filename = "{}.{}".format('sales', ext)
#     #         # return the whole path to the file
#     #         return os.path.join(path, filename)
#     #
#     #     return wrapper
#     #
#     # file = models.FileField(upload_to=path_and_rename('files/'), null=True)
#     # file = models.FileField(upload_to=path_and_rename, verbose_name=(u'sales'), null=True)
#
#     file = models.FileField(upload_to='files/', null=True)
#
#     def __repr__(self):
#         return 'AllSales(%s, %s)' % (self.name, self.file)
#
#     def __str__(self):
#         return self.name


class Result(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)

    def path_and_rename(path):  # потом добавить аргумент кого во что переименовать соответственно
        def wrapper(instance, filename):
            ext = filename.split(".")[-1]
            # g filename
            filename = "{}.{}".format('departments', ext)
            # return the whole path to the file
            return os.path.join(path, filename)

        return wrapper

    file = models.FileField(upload_to=path_and_rename('files/'), null=True)
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
    # cost_price = models.FloatField(null=True, blank=True, default=None)
    # quantity = models.FloatField(null=True, blank=True, default=None)
