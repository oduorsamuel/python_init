# Generated by Django 3.1.3 on 2021-01-08 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210108_1240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brand',
            old_name='category_id',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='brand',
            old_name='sub_category_id',
            new_name='sub_category',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='category_id',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='sub_category_id',
            new_name='sub_category',
        ),
        migrations.RenameField(
            model_name='subcategory',
            old_name='category_id',
            new_name='category',
        ),
    ]
