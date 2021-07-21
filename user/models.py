from django.contrib.auth.models import User
from django.db import models
# Create your models here.
"""
1.orm模型是一个类
2.必须继承models.Model
3.需要定义类属性-------字段，类名------表名
4.需要将当前应用添加到配置文件中的安装应用列表中 即seeting下的INSTALLED_APPS 
5.生成迁移文件--》将模型生成sql语句 即makemigrations 
6.执行迁移 即migrate---》执行sql
7.id主键自动生成
8.一旦修改重新生成执行迁移文件
"""

"""
    文章 分类
    文章 表
"""


class Category(models.Model):
    """
    分类表
    """
    name = models.CharField(max_length=50,verbose_name='分类名')
    brief = models.CharField(max_length=200,verbose_name='描述')
    add_time = models.DateTimeField(auto_now_add=True,verbose_name='添加时间')
    update_time = models.DateTimeField(auto_now=True,verbose_name='更新时间')
    isDel = models.BooleanField(default=False,verbose_name="是否删除")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "category"   #改表名
        verbose_name = "分类管理"
        verbose_name_plural = verbose_name



class Article(models.Model):
    """
    文章表
    """
    title = models.CharField(max_length=50,verbose_name="标题")
    brief = models.CharField(max_length=255,verbose_name="简介")
    author = models.ForeignKey(to=User, verbose_name="作者",on_delete=models.CASCADE)
    logo = models.ImageField(verbose_name="封面图", upload_to="article/%Y/%m/%d")
    content = models.TextField(verbose_name="内容")
    cateogry = models.ForeignKey(to="Category", verbose_name='文章分类',on_delete=models.CASCADE)
    hits = models.IntegerField(default=0, verbose_name='点击量')
    love_num = models.IntegerField(default=0, verbose_name='点赞数')

    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    isDel = models.BooleanField(default=False, verbose_name="是否删除")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "article"
        verbose_name = "文章管理"
        verbose_name_plural = verbose_name
