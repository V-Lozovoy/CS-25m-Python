from django.db import models

class University(models.Model):
    code = models.CharField('Код закладу в ЄДЕБО',max_length=4, unique=True)
    title = models.CharField('Назва університету',max_length=150)
    ownership = models.CharField('Форма власності', max_length=10)
    rector = models.CharField('Ім`я ректора',max_length=100)
    location = models.TextField('Місцезнаходження')
    phone = models.CharField('Телефон/факс', max_length=100)
    email = models.CharField('Електронна пошта', max_length=50)
    website = models.CharField('Вебсайт університету', max_length=120)
    military_department = models.CharField('Чи є військова кафедра', max_length=3)
    grants = models.CharField('Чи бере заклад участь в програмі державних грантів на здобуття вищої освіти', max_length=3)
    year = models.CharField('Рік заснування', max_length=4)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Університет'
        verbose_name_plural = 'Університети'