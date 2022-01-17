from django.contrib import admin
from .models import Book, Autor, BookType, PublishingHouse, BookList

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'pages', 'types', 'autors', 'edition')


class PublishingHouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'publish_date')

admin.site.register(Book, BookAdmin)
admin.site.register(Autor)
admin.site.register(BookType)
admin.site.register(PublishingHouse, PublishingHouseAdmin)
admin.site.register(BookList)
