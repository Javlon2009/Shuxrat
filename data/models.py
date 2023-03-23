from django.db import models

class person(models.Model):
    username = models.CharField('username' ,max_length=235)
    password = models.CharField('password', max_length=235)
    userid = models.CharField('id', max_length=30)

class data(models.Model):
    froms = models.CharField('Savol', max_length=200000035)
    to = models.CharField('javob', max_length=23000000000000005)
    userid = models.CharField('userid', max_length=30)

class nubm(models.Model):
    userid = models.CharField('userid', max_length=235)
    nubm = models.CharField('num', max_length=1000000000000)