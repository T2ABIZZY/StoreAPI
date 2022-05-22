# Generated by Django 4.0.3 on 2022-05-22 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0020_delete_likedposts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rooms',
            field=models.DecimalField(decimal_places=0, max_digits=2, null=True),
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='API/images')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='API.product')),
            ],
        ),
    ]