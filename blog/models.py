from django.db import models

# Create your models here.
class Blog(models.Model):
    pub_date = models.DateTimeField()
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

# add the blog app to the settings

# create a migration


# migrate

