from django.db import models

class Course(models.Model):
    img = models.ImageField(upload_to='media/img/')
    author = models.CharField(max_length=250)
    course = models.CharField(max_length=250)
    language = models.CharField(max_length=250)
    reyting = models.SmallIntegerField()
    
    def __str__(self):
        return self.author
