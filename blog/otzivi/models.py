from django.db import models

class Review(models.Model):
    full_name = models.CharField(max_length=200, verbose_name='ФИО', default='ФИО')
    email = models.CharField(max_length=200, verbose_name='Email', default='email') 
    review_text = models.TextField(verbose_name='Текст отзыва')
    show_on_site = models.BooleanField(default=False, verbose_name='Показывать на сайте')
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
    
    def __str__(self):
        return f"{self.full_name}"