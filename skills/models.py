from django.db import models

# Create your models here.
class ProgrammingKnowledge(models.Model):
    """A typical class defining a model, derived from the Model class."""
    title = models.CharField(max_length = 100)
    desc  = models.CharField(max_length = 400)
    img   = models.ImageField(upload_to='skills/images')
    url   = models.URLField()

    def __str__(self):
        return self.title