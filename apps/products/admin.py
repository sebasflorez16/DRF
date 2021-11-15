from django.contrib import admin

# Register your models here.
from apps.products.models import * 

class MeasureAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')


admin.site.register(MeasureUnit, MeasureAdmin)
admin.site.register(CategoryProduct, CategoryAdmin)
admin.site.register(Indicator)
admin.site.register(Product)
