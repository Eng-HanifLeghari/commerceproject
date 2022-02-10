from django.contrib import admin
from .models import Category, Subcategory, ProductImage, Product, ProductDiscription, AditionalInform, Reviews

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'discription', 'discount', 'category', 
    'subcategory', 'trend', 'off', 'spacification', 'is_slider']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['name',  'category']

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['image', 'product']


@admin.register(ProductDiscription)
class ProductDiscriptionAdmin(admin.ModelAdmin):
    # fields = ("__all__")
    list_display = ['product', 'title1_image', 'title1_heading', 'title1_discription',
                    'title2_image', 'title2_heading', 'title2_discription',
                    'title3_image', 'title3_heading', 'title3_discription',
                    'title4_image', 'title4_heading', 'title4_discription',
                    'title5_image', 'title5_heading', 'title5_discription',]


@admin.register(AditionalInform)
class AditionalInformAdmin(admin.ModelAdmin):
    list_display = ['product', 'capacity', 'Weight_Dimensions', 'display', 'iSight_Camera', 'VideoRecording']


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'comment', 'get_rate', 'created_at', 'title']


