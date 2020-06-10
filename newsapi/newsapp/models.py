from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(("Description"))



    created_at = models.DateTimeField(("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(("Updated at"), auto_now=True)

        

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

        ordering = ['name']

    def __str__(self):
        return self.name


class News(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField('news', max_length=50)
    description = models.TextField(("Description"))
    image = models.ImageField(upload_to='newsmedia/',null=True,blank=True)

    # slug = models.SlugField(unique=True)
    
    created_at = models.DateTimeField(("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(("Updated at"), auto_now=True)

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

        ordering = ['name']

    def __str__(self):
        return self.name




