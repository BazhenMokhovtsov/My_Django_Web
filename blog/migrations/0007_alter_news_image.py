# Generated by Django 4.0.8 on 2024-04-13 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_news_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(upload_to='blog/%Y/%m/%d/', verbose_name='Image'),
        ),
    ]
