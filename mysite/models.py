from django.db import models

class invmm(models.Model):
  accountno = models.CharField(max_length=16)
  name = models.CharField(max_length=30)
  openingbal = models.CharField(max_length=14)
  mobilenumber = models.CharField(max_length=14)
  email = models.CharField(max_length=30)
  narration = models.CharField(max_length=30)


class master(models.Model):
  accountno = models.CharField(max_length=16)
  name = models.CharField(max_length=30)
  openingbal = models.CharField(max_length=14)
  mobilenumber = models.CharField(max_length=14)
  email = models.CharField(max_length=30)
  narration = models.CharField(max_length=30)


class passbook(models.Model):
  accno = models.CharField(max_length=16)
  name = models.CharField(max_length=30)
  balbefore = models.CharField(max_length=14)
  balafter = models.CharField(max_length=14)
  dateoftran = models.CharField(max_length=16)
  crdr = models.CharField(max_length=2)
  narration = models.CharField(max_length=30)