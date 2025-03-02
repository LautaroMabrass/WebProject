from django.contrib import admin
from .models import Post, Category  # Importar modelos correctamente

# Personalización del panel de administración para Categoría
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

# Personalización del panel de administración para Post
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

# Registrar los modelos con sus clases de administración
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
