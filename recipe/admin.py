from django.contrib import admin
from recipe.models import Recipe

class RecipeAdin(admin.ModelAdmin):
    list_display = ('id','title')

admin.site.register(Recipe,RecipeAdin)

# Register your models here.
