# Generated by Django 3.2.7 on 2021-10-25 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20211020_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='/sample.jpg', null=True, upload_to=''),
        ),
    ]