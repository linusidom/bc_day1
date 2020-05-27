# Generated by Django 3.0.6 on 2020-05-26 04:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0001_initial'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='billing_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='billing_adress', to='addresses.Address'),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping',
            field=models.DecimalField(blank=True, decimal_places=2, default=60, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_adress',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shipping_adress', to='addresses.Address'),
        ),
    ]