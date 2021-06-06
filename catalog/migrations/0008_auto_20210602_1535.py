# Generated by Django 3.2.3 on 2021-06-02 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20210602_1506'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='size_shoes',
        ),
        migrations.AddField(
            model_name='size',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sizes', to='catalog.category'),
        ),
        migrations.DeleteModel(
            name='Size_shoes',
        ),
    ]