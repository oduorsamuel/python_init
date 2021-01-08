# Generated by Django 3.1.3 on 2021-01-08 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='sub_category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.subcategory'),
        ),
        migrations.AlterField(
            model_name='products',
            name='brand_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.brand'),
        ),
        migrations.AlterField(
            model_name='products',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category'),
        ),
        migrations.AlterField(
            model_name='products',
            name='sub_category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.subcategory'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category'),
        ),
    ]
