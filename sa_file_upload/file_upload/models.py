from django.db import models

class Student(models.Model):
    rollNumber = models.IntegerField(default = 0,unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    antiragging_students = models.FileField(upload_to= 'antiragging/students', default=None,max_length = 100)
    antiragging_parents = models.FileField(upload_to='antiragging/parents',default=None, max_length = 100)
    code_conduct = models.FileField(upload_to='code_conduct',default=None, max_length = 100)
    undertaking_hostel = models.FileField(upload_to='undertaking_hostel', default=None,max_length = 100)

    def __str__(self):
        return self.name + '-' + str(self.rollNumber) # TODOOP