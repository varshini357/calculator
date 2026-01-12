from django.db import models

class AllOperations(models.Model):
    operation = models.CharField(max_length=10)
    number1 = models.FloatField()
    number2 = models.FloatField()
    result = models.FloatField()

class AdditionResult(models.Model):
    number1 = models.FloatField()
    number2 = models.FloatField()
    result = models.FloatField()

class SubtractionResult(models.Model):
    number1 = models.FloatField()
    number2 = models.FloatField()
    result = models.FloatField()

class MultiplicationResult(models.Model):
    number1 = models.FloatField()
    number2 = models.FloatField()
    result = models.FloatField()

class DivisionResult(models.Model):
    number1 = models.FloatField()
    number2 = models.FloatField()
    result = models.FloatField()
