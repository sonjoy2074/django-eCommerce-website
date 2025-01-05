from django.db import models
# Create your models here.

class Category(models.Model):
    tittle = models.CharField(max_length=264, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tittle
    
    class Meta:
        verbose_name_plural = 'Categories'

class Product(models.Model):
    mainimage = models.ImageField(upload_to='products')
    name = models.CharField(max_length=264,)
    catagory = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    preview_text = models.TextField(max_length=200, verbose_name='Preview Text') 
    detail_text = models.TextField(max_length=1000, verbose_name='Detail Text')
    price = models.FloatField()
    old_price = models.FloatField(default=0.00)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('-created_date',)
        verbose_name_plural = 'Products'
