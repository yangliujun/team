#coding: utf-8
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
# Create your models here.
class VipLlist(models.Model):
    MemberID = models.CharField(max_length=50,unique=True)
    Password = models.CharField(max_length=50,unique=True)
    TrueName = models.CharField(max_length=10,unique=True)
    Phonecode = models.CharField(max_length=50,unique=True)
    Email = models.CharField(max_length=50,unique=True)
    Address = models.TextField(max_length=200,unique=True)
    PostCode = models.CharField(max_length=20,unique=True)
class OrderList(models.Model):
    OrderID = models.CharField(max_length=50,unique=True)
    Vip_MemberID = models.ForeignKey('MemberID')
    OrderDate = date.day()
    GoodsFree = models.CharField(max_length=20,unique=True)
    TotalPrice = models.CharField(max_length=20,unique=True)
    ShipType = models.CharField(max_length=20,unique=True)
    PayType = models.CharField(max_length=20,unique=True)
    ReceiverName = models.CharField(max_length=20,unique=True)
    ReceiverPhone = models.CharField(max_length=20,unique=True)
    ReceiverPostCode = models.CharField(max_length=20,unique=True)
    ReceiverAddress = models.TextField(max_length=200,unique=True)
class ShoppingCart(models.Model):
    CatID = models.CharField
    