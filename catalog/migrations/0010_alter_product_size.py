# Generated by Django 3.2.3 on 2021-06-02 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20210602_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.ManyToManyField(blank=True, related_name='products', to='catalog.Size'),
        ),
    ]