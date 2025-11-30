from django.contrib import admin
from .models import Restaurant,Category
from django.utils.safestring import mark_safe

# Register your models here.
class RestaurantAdmin(admin.ModelAdmin):
  list_display=('id','name','price','address','image','category')
  search_fields=('name',)
  list_filter=('category',)

  def image(self,obj):
    return mark_safe('<img src="{}" style="width:100px height:auto;">'.format(obj.img.url))

class CategoryAdmin(admin.ModelAdmin):
  list_display=('id','name')
  search_fields=('name',)


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Category,CategoryAdmin)

