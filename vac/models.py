from django.db import models

from job.models import Company


class Category(models.Model):
    JOB_CHOICES = (
        ('IT','IT'),
        ('Engineering','Engineering'),
        ('Jurist','Jurist'),
        ('Economist','Economist'),
        ('Doctor','Doctor'),
    )
    title = models.CharField(max_length=255)
    job = models.CharField(choices=JOB_CHOICES, blank=True, null=True, max_length=30)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 blank=True, null=True, related_name='posts')
    author = models.ForeignKey(Company, on_delete=models.SET_NULL,
                               blank=True, null=True, related_name='author_posts')
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='posts', blank=True, null=True)
    rating = models.FloatField(default=0)
    seen_amount = models.PositiveIntegerField(default=0)
    published = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return self.title

