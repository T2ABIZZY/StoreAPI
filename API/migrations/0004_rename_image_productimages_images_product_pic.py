# Generated by Django 4.0.3 on 2022-05-22 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_alter_productimages_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productimages',
            old_name='image',
            new_name='images',
        ),
        migrations.AddField(
            model_name='product',
            name='pic',
            field=models.FileField(null=True, upload_to='API/images'),
        ),
    ]
