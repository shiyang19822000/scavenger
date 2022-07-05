# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class CompensationModel(models.Model):
    cpns_id = models.BigAutoField(primary_key=True, verbose_name="赔偿方案编号")
    cpns_title = models.CharField(max_length=128, null=False, blank=True, verbose_name="赔偿方案标题")
    cpns_category = models.IntegerField(choices=((1, 'N'),
                                                 (2, 'N1'),
                                                 (3, 'N2')),
                                        default=1,
                                        verbose_name='赔偿方案分类')
    cpns_content = RichTextField(null=False, blank=True, verbose_name="赔偿方案内容")
    activated = models.IntegerField(choices=((0, '未激活'),
                                             (1, '已激活')),
                                    default=1,
                                    verbose_name='数据状态')
    create_at = models.DateTimeField(auto_now_add=True, null=False, verbose_name="创建时间")
    update_at = models.DateTimeField(auto_now=True, null=False, verbose_name="更新时间")

    def __str__(self):
        return self.cpns_title

    class Meta:
        managed = True
        verbose_name = "Compensation"
        verbose_name_plural = "Compensations"
        db_table = "compensation"
        ordering = ['-update_at']
