from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'Djangoku'

    def __str__(self):
        return self.title