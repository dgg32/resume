from django.db import models

# Create your models here.
class Blog(models.Model):
    pub_date = models.DateTimeField()
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return " ".join(self.body.split(" ")[:10]) + " ..."
    
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
# add the blog app to the settings

# create a migration


# migrate

