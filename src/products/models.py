from django.conf import settings
from django.db import models
from django.core.files.storage import FileSystemStorage

def download_media_location(instance, filename):
    return '%s/%s' % (instance.id, filename)

# Create your models here.
class Product(models.Model):
    #user = models.ForeignKey('User', on_delete=models.PROTECT)
    media = models.FileField(blank=True,
                            null=True,
                            upload_to=download_media_location,
                            storage=FileSystemStorage(location=settings.PROTECTED_ROOT))
    title = models.CharField(max_length=30) # holds characters
    description = models.TextField(default=True)
    price = models.DecimalField(max_digits=100, decimal_places=2)

    def __str__(self):
        return self.title

class User(models.Model):
    pass
