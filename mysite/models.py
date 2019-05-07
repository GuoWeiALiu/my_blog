from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


# 继承系统的user 自定义user
class User(AbstractUser):
    # 手机号
    phone = models.CharField(verbose_name="手机号码", max_length=11, null=True, unique=True)
    # 昵称
    nickname = models.CharField(verbose_name="昵称", max_length=25, null=True)
    # 头像
    avatar = models.URLField(verbose_name="头像", null=True)
    # 信息修改时间
    modify_date = models.DateTimeField(verbose_name="最后修改时间", auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.username, self.email)


class ArticleCategory(models.Model):
    '''文章分类'''
    name = models.CharField("分类名称", max_length=20)
    created_date = models.DateTimeField("创建时间", auto_now_add=True)

    class Meta:
        verbose_name = '文章分类'
        verbose_name_plural = verbose_name

    def _str_(self):
        return self.name


class ArticleTag(models.Model):
    ''' 文章标签 '''
    name = models.CharField('标签名称', max_length=20)
    slug = models.SlugField(default='no-slug', max_length=60, blank=True)
    created_date = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:tag_detail', kwargs={'tag_name': self.slug})


class Article(models.Model):
    '''文章'''
    STATUS_CHOICES = (
        (0, '草稿'),
        (1, '发表'),
    )

    title = models.CharField('文章标题', max_length=50, null=False)
    content = models.TextField('文章内容', null=False)

    pub_date = models.DateTimeField('发布时间', auto_now_add=True)
    last_mod_date = models.DateTimeField('最后修改时间', auto_now_add=True)

    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)
    status = models.IntegerField('文章状态', choices=STATUS_CHOICES, default=0)
    category = models.ForeignKey(ArticleCategory, verbose_name='分类', on_delete=models.CASCADE, blank=False, null=False)

    views = models.IntegerField('浏览量', default=0)

    tags = models.ManyToManyField(ArticleTag, verbose_name='标签', blank=True)

    # 元数据，
    class Meta:
        # 文章排序规则
        ordering = ['-pub_date']
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        get_latest_by = 'id'
