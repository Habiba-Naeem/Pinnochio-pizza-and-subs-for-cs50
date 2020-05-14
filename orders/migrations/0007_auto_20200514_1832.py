# Generated by Django 2.2.10 on 2020-05-14 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20200509_1653'),
    ]

    operations = [
        migrations.CreateModel(
            name='No_of_Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topping', models.CharField(choices=[('C', 'Cheese'), ('one', '1 topping'), ('two', '2 toppings'), ('three', '3 toppings'), ('five', '5 toppings')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('S', 'Small'), ('L', 'Large')], max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='dinnerplatters',
            name='platter',
        ),
        migrations.RemoveField(
            model_name='dinnerplatters',
            name='price',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='pizza',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='price',
        ),
        migrations.AlterField(
            model_name='dinnerplatters',
            name='size',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Size'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='size',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Size'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='topping',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.No_of_Topping'),
        ),
        migrations.CreateModel(
            name='Sicilian_Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pizza', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Pizza')),
            ],
        ),
        migrations.CreateModel(
            name='Regular_Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pizza', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Pizza')),
            ],
        ),
        migrations.CreateModel(
            name='Platter_Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('platter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.DinnerPlatters')),
            ],
        ),
    ]
