# Generated by Django 4.1.3 on 2022-12-06 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0010_profileproduct_product_profiles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ProfileProduct', to='phones.product'),
        ),
    ]
