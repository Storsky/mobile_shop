# Generated by Django 4.1.3 on 2022-12-01 08:46

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0003_alter_model_id_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=['model_id', 'color']),
        ),
    ]
