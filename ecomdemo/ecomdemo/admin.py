from django.contrib import admin
from ecomdemo.models import User, Product

# admin.site.register(User)
# admin.site.register(Product)

#we can regsiter in two ways with annotation and with dot operator
#the annotation part helps with customisation like adding search field , filters and so on
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ['title', 'username', 'name', 'email']
    list_display = ['username', 'name', 'email', 'address']
    search_fields = ['name']
    list_filter = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # fields = ['seller', 'name', 'price', 'description', 'stock']
    list_display = ['id', 'name', 'price']
    search_fields = ['id',]
    list_filter = ['price']
    save_on_top = True
    fieldsets = (
        ("Product Info", {
            'fields': ('seller', 'name', 'description')
        }
         ),
        ("Stock Info", {
            'fields': ('price', 'stock'),
            'classes': ('collapse',)
        })
    )

