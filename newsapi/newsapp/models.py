from django.db import models
# from django.utils.text import slugify
from django.template.defaultfilters import slugify

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

    slug = models.SlugField(max_length=500,unique=True,blank=True)
    created_at = models.DateTimeField(("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(("Updated at"), auto_now=True)

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

        ordering = ['name']

    def save(self, **kwargs):
        if not self.slug:
            slug = slugify(self.name)
            while True:
                try:
                    news = News.objects.get(slug=slug)
                    if news == self:
                        self.slug = slug
                        break
                    else:
                        slug = slug + '-'
                except:
                    self.slug = slug
                    break

        super(News, self).save()
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super(News, self).save(*args, **kwargs)
        

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     i=0
    #     while self.slug == self.slug:

    #         self.slug = self.slug + str(i)
    #         i = i + 1
    #     return super(News, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.name




