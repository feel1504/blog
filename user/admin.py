from django.contrib import admin
from user.models import Article, Category

# Register your models here.
"""
    在admin显示的两中方式
        第一种：
            admin.site.register(模型类名)；
            自定义效果，定义一个后台管理类
        第二种
"""
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["id","title",'author','cateogry',"brief","add_time",'update_time']
    list_display_links = ['id',"title",'author','cateogry',"brief"] #点击对应的内容可以进入修改界面
    list_per_page = 10  #每页显示几条
admin.site.register(Article,ArticleAdmin)   #第一种方式
#@admin.site.register(Article) 这是第二种方式

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id","name","brief","add_time",'update_time']
    list_display_links = ['id',"name","brief"] #点击对应的内容可以进入修改界面
    list_per_page = 10  #每页显示几条
admin.site.register(Category,CategoryAdmin)

