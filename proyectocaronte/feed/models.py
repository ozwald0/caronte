import datetime
from email.policy import default
from enum import unique
from time import timezone
from django.db import models
from django.contrib.auth.models import User


#class Level(models.Model):
#    level_name = models.CharField(max_length = 200, unique = True, blank = True)
#    description = models.TextField()
#    created = models.DateTimeField(auto_now_add = True)
#    updated = models.DateTimeField(auto_now = True)
#    
#
#    def __str__(self):
#        return self.level_name


#class StatusOfUsers(models.Model):
#    status_of_users_name = models.CharField(max_length = 200, unique = True)
#    created = models.DateTimeField(auto_now_add = True)
#    updated = models.DateTimeField(auto_now = True)
#    
#    def __str__(self):
#        return self.status_of_users_name


#class User(models.Model):
#    level_name = models.ForeignKey(Level, on_delete = models.DO_NOTHING, blank = True, default= 1)
#    status_of_users_name = models.ForeignKey(StatusOfUsers, on_delete = models.DO_NOTHING, blank = True, default = 1)
#    name = models.CharField(max_length = 200)
#    passwd = models.CharField(max_length = 200)
#    email = models.CharField(max_length = 200)
#    created = models.DateTimeField(auto_now_add = True)
#    updated = models.DateTimeField(auto_now = True)
#    
#    def __str__(self):
#        return self.name

    

class Client(models.Model):
    name = models.CharField(max_length = 200)
    company_name = models.CharField(max_length = 200, blank = True)
    email = models.CharField(max_length = 200, blank = True, unique = True)
    phonenumber = models.CharField(max_length = 200, blank = True)
    adress = models.TextField(blank = True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.name


class TypeOfItem(models.Model):
    description = models.CharField(max_length = 200, unique = True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.description



class Item(models.Model):
    type_of_item = models.ForeignKey(TypeOfItem, on_delete = models.DO_NOTHING)
    model = models.CharField(max_length = 200, unique = True)
    brand = models.CharField(max_length = 200)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.model


class ClientComment(models.Model):
    client = models.ForeignKey(Client, on_delete = models.DO_NOTHING)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)


class TypeOfProduct(models.Model):
    description = models.CharField(max_length = 200, unique = True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.description


class Status(models.Model):
    name = models.CharField(max_length = 200, unique = True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name


class TypeOfService(models.Model):
    name = models.CharField(max_length = 200, unique = True) 
    price = models.DecimalField(max_digits = 9, decimal_places = 2)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name


class Service(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    service_type = models.ForeignKey(TypeOfService, on_delete = models.DO_NOTHING)
    type_of_product = models.ForeignKey(TypeOfProduct, on_delete = models.DO_NOTHING)
    client = models.ForeignKey(Client, on_delete = models.CASCADE)
    status = models.ForeignKey(Status, on_delete = models.DO_NOTHING)
    model = models.CharField(max_length = 200, blank = True)
    serial_number = models.CharField(max_length = 200, blank = True)
    accesories = models.CharField(max_length = 200, blank = True)
    failure = models.TextField()
    is_working = models.BooleanField() 
    is_damaged = models.BooleanField()
    is_complete = models.BooleanField()
    service_reference = models.CharField(max_length = 200)
    service_price = models.DecimalField(max_digits = 9, decimal_places = 2)
    client_pass = models.CharField(max_length = 200, unique = True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.failure


class ServiceComment(models.Model):
    service = models.ForeignKey(Service, on_delete = models.DO_NOTHING)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.comment


class ItemDetail(models.Model):
    service = models.ForeignKey(Service, on_delete = models.DO_NOTHING)
    item = models.ForeignKey(Item, on_delete = models.DO_NOTHING)
    serial_number = models.CharField(max_length = 200, unique = True)
    reference = models.CharField(max_length = 200)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)








