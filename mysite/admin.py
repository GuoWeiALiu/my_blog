from django.contrib import admin

# Register your models here.
from mysite.models import User, ArticleTag, ArticleCategory, Article


# @admin.register(User)  装饰器 和 函数注册是一样的效果
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "phone", "email", "nickname", "date_joined")


admin.site.register(User, UserAdmin)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # 展示的字段
    list_display = ('title', 'pub_date', 'author', 'views')
    # 添加文章的时候，选择标签 横排显示
    filter_horizontal = ('tags',)


@admin.register(ArticleTag)
class ArticleTagAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_date')
    # 不显示在后台
    exclude = ('slug',)


@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_date')
