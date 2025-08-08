from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13)
    project = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
class Blog(models.Model):
    title = models.CharField(max_length=250)
    created_date = models.DateField(auto_now=True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,blank=True,null=True)
    content = models.TextField()
    image = models.ImageField(upload_to="Blog/")

    def __str__(self):
        return f"{self.title[:20]}..."

class Team(models.Model):
    full_name = models.CharField(max_length=250)
    job = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team_images/', null=True, blank=True)


    def __str__(self):
        return f"{self.full_name[:20]}..."
    