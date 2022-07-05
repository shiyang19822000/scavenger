# Generated by Django 4.0.4 on 2022-05-06 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleModel',
            fields=[
                ('art_id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='文章编号')),
                ('art_title', models.CharField(blank=True, max_length=64, verbose_name='文章标题')),
                ('art_publisher', models.CharField(blank=True, max_length=32, verbose_name='文章发布者')),
                ('art_content', models.TextField(blank=True, verbose_name='文章内容')),
                ('art_declaration', models.TextField(blank=True, verbose_name='文章声明')),
                ('art_thumbnail', models.CharField(blank=True, max_length=128, verbose_name='文章缩略图')),
                ('art_illustrated', models.CharField(blank=True, max_length=128, verbose_name='文章插图')),
                ('art_category', models.IntegerField(choices=[(1, '莫慌'), (2, '别闹')], default=0, verbose_name='文章分类')),
                ('art_status', models.IntegerField(choices=[(1, '未发布'), (2, '已发布')], default=0, verbose_name='文章状态')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '文章表',
                'verbose_name_plural': '文章表',
                'db_table': 'article',
                'managed': True,
            },
        ),
    ]