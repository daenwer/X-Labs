from django.contrib import admin
from main.models import Author, Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Author._meta.fields]


class BookAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Book._meta.fields]


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
