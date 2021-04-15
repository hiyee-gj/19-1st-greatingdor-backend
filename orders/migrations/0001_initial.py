# Generated by Django 3.2 on 2021-04-15 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_name', models.CharField(max_length=45)),
                ('to_email', models.CharField(max_length=45)),
                ('to_phone_number', models.CharField(max_length=45)),
                ('reciever_name', models.CharField(max_length=45)),
                ('reciever_phone_number', models.CharField(max_length=45)),
                ('reciever_number', models.CharField(max_length=45)),
                ('reciever_message', models.CharField(max_length=45)),
                ('shipping_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('post_number', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=300)),
                ('address_detail', models.CharField(max_length=300)),
                ('progress_status', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.member')),
            ],
            options={
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('discount_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('product_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productoption')),
            ],
            options={
                'db_table': 'order_products',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.member')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_product', to='products.product')),
                ('product_option', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.productoption')),
            ],
            options={
                'db_table': 'carts',
            },
        ),
    ]
