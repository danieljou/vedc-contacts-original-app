from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(PhotoAssemble)
admin.site.register(Assemblee)
admin.site.register(Programme)