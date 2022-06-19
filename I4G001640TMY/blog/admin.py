from django.contrib import admin

# blog app models.

from .models import blog

# Register blog in the admin site

admin.site.register(blog)
