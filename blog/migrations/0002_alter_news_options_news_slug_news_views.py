# Generated by Django 4.0.8 on 2024-04-12 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'New', 'verbose_name_plural': 'News'},
        ),
        migrations.AddField(
            model_name='news',
            name='slug',
            field=models.SlugField(auto_created=True, default='exit', verbose_name='Slug'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='views',
            field=models.IntegerField(default=1, verbose_name='Views'),
        ),
    ]