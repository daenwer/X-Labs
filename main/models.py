from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
        
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ('last_name',)


class Book(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    year_of_publishing = models.IntegerField()
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="books"
    )
    
    def __str__(self) -> str:
        return f'{self.name}: {self.year_of_publishing}'
    
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ('name', 'year_of_publishing')
