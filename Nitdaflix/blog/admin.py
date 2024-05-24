from django.contrib import admin

from blog.models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    exclude = ()

