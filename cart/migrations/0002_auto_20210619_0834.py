# Generated by Django 3.2.3 on 2021-06-19 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promo', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Промо-код',
                'verbose_name_plural': 'Промо-коды',
            },
        ),
        migrations.AlterModelOptions(
            name='mart',
            options={'verbose_name': 'Магазин', 'verbose_name_plural': 'Магазины'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
    ]
