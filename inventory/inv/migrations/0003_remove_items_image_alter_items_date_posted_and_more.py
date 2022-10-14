# Generated by Django 4.1.2 on 2022-10-08 09:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("inv", "0002_items_desc_items_num_alter_items_image_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="items", name="image",),
        migrations.AlterField(
            model_name="items",
            name="date_posted",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="items",
            name="type",
            field=models.CharField(default="*type*", max_length=100),
        ),
    ]
