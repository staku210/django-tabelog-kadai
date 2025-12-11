from django.contrib import admin
from .models import Restaurant,Category,Review,Reservation,CustomUser,Favorite
from django.utils.safestring import mark_safe
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class RestaurantAdmin(admin.ModelAdmin):
  list_display=('id','name','price','address','phone','description','image','category')
  search_fields=('name','address','phone')
  list_filter=('category',)

  def image(self,obj):
    return mark_safe('<img src="{}" style="width:100px height:auto;">'.format(obj.img.url))

class CategoryAdmin(admin.ModelAdmin):
  list_display=('id','name')
  search_fields=('name',)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'user', 'rating', 'comment', 'created_at')
    list_filter = ('restaurant', 'rating', 'created_at')
    search_fields = ('user__username', 'comment')

class ReservationAdmin(admin.ModelAdmin):
   list_display=('restaurant','user','date','time','number_of_people')
   list_filter=('restaurant','user','date','time')
   search_fields=('user__username','restaurant')


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'restaurant')
    search_fields = ('user__username', 'restaurant__name')


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active', 'is_premium')
    list_filter = ('is_staff', 'is_active', 'is_premium')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_premium')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Stripe', {'fields': ('stripe_customer_id',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active', 'is_premium')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Review,ReviewAdmin)
admin.site.register(Reservation,ReservationAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(CustomUser,CustomUserAdmin)

