from django.db import models

class Item(models.Model):
    name = models.CharField( max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    images = models.ImageField(blank=True, upload_to='images')
    mp3_file = models.FileField(upload_to='mp3_files')
    
    def __str__(self) -> str:
        return self.name