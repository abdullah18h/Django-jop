from django.db import models

# Create your models here.

## models.Model inher from it becaus :
# to get fields 

'''
django model field
    -html widget
    -validation
    -db.size
    -
'''

class Category(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name
    

class Jop(models.Model): # it like table in database

    j_type=[
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time')
    ]
  
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=15, choices=j_type)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    exper = models.IntegerField(default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

