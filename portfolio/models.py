from django.db import models

class HomeContent(models.Model):
    headline = models.CharField(max_length=200)
    subheadline = models.CharField(max_length=300, blank=True)
    background_image = models.ImageField(upload_to='home/', blank=True)

    def __str__(self):
        return self.headline

class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    profile_image = models.ImageField(upload_to='about/', blank=True)

    def __str__(self):
        return self.title

class Service(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, help_text="FontAwesome icon class")
    description = models.TextField()

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(help_text="10")

    def __str__(self):
        return f"{self.name} ({self.proficiency}%)"

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
