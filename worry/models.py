# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class ArticleModel(models.Model):
    art_id = models.BigAutoField(primary_key=True, verbose_name="文章编号")
    art_title = models.CharField(max_length=128, null=False, blank=True, verbose_name="文章标题")
    art_source = models.IntegerField(choices=((1, '自撰'),
                                              (2, '转载')),
                                     default=2,
                                     verbose_name='文章来源')
    art_publisher = models.CharField(max_length=64, null=False, blank=True, verbose_name="发布者")
    publish_time = models.DateTimeField(null=False, blank=True, verbose_name="发表时间")
    # art_content = models.TextField(null=False, blank=True, verbose_name="文章内容")
    art_content = RichTextField(null=False, blank=True, verbose_name="文章内容")
    # art_declaration = models.TextField(null=False, blank=True, verbose_name="文章声明")
    art_declaration = RichTextField(null=False, blank=True, verbose_name="文章声明")
    art_thumbnail = models.CharField(max_length=256, null=False, blank=True, verbose_name="缩略图")
    art_illustrated = models.CharField(max_length=256, null=False, blank=True, verbose_name="文章插图")
    art_category = models.IntegerField(choices=((1, '莫慌'),
                                                (2, '别闹')),
                                       default=1,
                                       verbose_name='文章分类')
    art_status = models.IntegerField(choices=((1, '未发布'),
                                              (2, '已发布')),
                                     default=1,
                                     verbose_name='文章状态')
    activated = models.IntegerField(choices=((0, '未激活'),
                                             (1, '已激活')),
                                    default=1,
                                    verbose_name='数据状态')
    create_at = models.DateTimeField(auto_now_add=True, null=False, verbose_name="创建时间")
    update_at = models.DateTimeField(auto_now=True, null=False, verbose_name="更新时间")

    def __str__(self):
        return self.art_title

    class Meta:
        managed = True
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        db_table = "article"
        ordering = ['-update_at']
