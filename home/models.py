from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    decs= models.TextField()
    time =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    decs = models.TextField()

    def __str__(self):
        return self.name


