from django.db import models

class Item(models.Model):
    name = models.CharField( max_length=50)
    price = models.IntegerField()
    phone = models.IntegerField(null=True)
    description = models.CharField(max_length=200)
    text = models.CharField(default='Ваше значение по умолчанию', max_length=255)
    images = models.ImageField(blank=True, upload_to='images')
    mp3_file = models.FileField(upload_to='mp3_files')
    
    def __str__(self) -> str:
        return self.name