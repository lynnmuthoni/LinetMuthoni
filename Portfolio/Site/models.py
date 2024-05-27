from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    timeline = models.CharField(max_length=200)
    programming_languages = models.CharField(max_length=200)
    images = models.ImageField(upload_to='project_images/')
    furtherdescription = models.TextField()

    def __str__(self):
        return self.name
    @property
    def get_imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    
class Qualification(models.Model):
    title = models.CharField(max_length=200)
    startdate = models.DateField()
    enddate = models.DateField()
    description = models.TextField()
    services = models.TextField()

    def __str__(self):
        return self.title
    
    
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    details = models.TextField()
    images = models.ImageField(upload_to='project_images/')

    def __str__(self):
        return self.name
    @property
    def get_imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name