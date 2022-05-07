from django.contrib import admin
from .models import *
from django.utils.html import mark_safe
@admin.register(category.Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('name','description','image_view',)
    readonly_fields = ('url',)
    def image_view(self,obj):
        return mark_safe(f'<img src ="{obj.image.url}"  width="100" height="110" />')

    image_view.short_description = 'Изображение'
    image_view.allow_tags = True

@admin.register(subcategory.SubCategory)
class AdminSubCategory(admin.ModelAdmin):
    list_display = ('name', 'description', 'image_view',)
    readonly_fields = ('url',)

    def image_view(self, obj):
        return mark_safe(f'<img src ="{obj.image.url}"  width="100" height="110" />')

    image_view.short_description = 'Изображение'
    image_view.allow_tags = True
@admin.register(model.Model)
class AdminModel(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(item.ImageItems)
class AdminItemImages(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(item.ReviewsItem)
class AdminItemReviews(admin.ModelAdmin):
    list_display = ('name',)
@admin.register(item.Item)
class AdminItem(admin.ModelAdmin):
    list_display = ('name','description','image_view',)
    readonly_fields = ('url',)
    def image_view(self, obj):
         return mark_safe(f'<img src ="{obj.image.url}"  width="100" height="110" />')
    image_view.short_description = 'Изображение'
    image_view.allow_tags = True

@admin.register(quiz_result_student.QuizResult)
class AdminQuiz(admin.ModelAdmin):
    list_display = ('pk','question_number','question_type','result')

@admin.register(user.Users)
class AdminUser(admin.ModelAdmin):
   list_display = ('pk','image_view')
   def image_view(self,obj):
       return mark_safe(f'<img src ="{obj.image.url}"  width="100" height="110" />')
