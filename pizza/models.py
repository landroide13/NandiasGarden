from django.db import models


class Size(models.Model):
    title = models.CharField(max_length=70)

    def __str__(self):
        return self.title

class Topping1(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Topping2(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title        

class Pizza(models.Model):
    topping1 = models.ForeignKey(Topping1, on_delete=models.CASCADE)
    topping2 = models.ForeignKey(Topping2, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)












