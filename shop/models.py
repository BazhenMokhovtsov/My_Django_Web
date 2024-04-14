from django.db import models
from django.utils import timezone 


class Category(models.Model):
    title= models.CharField(max_length= 255)
    created_at = models.DateTimeField(default=timezone.now)
    class Meta:
        # The name of the model in the singular
        verbose_name = 'Category'
        # Model name in the plural
        verbose_name_plural = 'Categorys'

    def __str__(self):
        return self.title

class Course(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    students_qty = models.IntegerField()
    reviews_qty = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    images = models.ImageField(blank=True, upload_to='images')

    class Meta:
        # The name of the model in the singular
        verbose_name = 'Course'
        # Model name in the plural
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.title


class Image(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images')
    course = models.OneToOneField(Course, on_delete=models.CASCADE, related_name='course_image')
   
    def __str__(self):
        return self.title
    
