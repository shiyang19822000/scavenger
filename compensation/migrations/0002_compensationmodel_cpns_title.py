# Generated by Django 4.0.4 on 2022-06-05 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compensation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='compensationmodel',
            name='cpns_title',
            field=models.CharField(blank=True, max_length=128, verbose_name='赔偿方案标题'),
        ),
    ]