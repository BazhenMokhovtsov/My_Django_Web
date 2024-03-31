# Generated by Django 4.0.8 on 2024-03-17 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_course_image_delete_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='image',
            new_name='images',
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('course', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='course_image', to='shop.course')),
            ],
        ),
    ]
