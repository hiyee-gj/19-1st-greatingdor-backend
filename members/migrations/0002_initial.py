# Generated by Django 3.2 on 2021-04-15 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
        ('members', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='product_cart',
            field=models.ManyToManyField(related_name='cart', through='orders.Cart', to='products.Product'),
        ),
        migrations.AddField(
            model_name='member',
            name='product_favorite',
            field=models.ManyToManyField(related_name='user_favorite', through='members.UserFavorite', to='products.Product'),
        ),
        migrations.AddField(
            model_name='destination',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.member'),
        ),
    ]
