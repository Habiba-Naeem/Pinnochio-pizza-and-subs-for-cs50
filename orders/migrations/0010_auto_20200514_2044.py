# Generated by Django 2.2.10 on 2020-05-14 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_auto_20200514_2027'),
    ]

    operations = [
        migrations.CreateModel(
            name='Extra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extra', models.CharField(blank=True, max_length=20)),
                ('price_of_extra', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subs_Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub', models.CharField(max_length=20)),
                ('sub_choice', models.CharField(max_length=20)),
                ('extra', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Extra')),
                ('size', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Size')),
            ],
        ),
        migrations.RemoveField(
            model_name='subs',
            name='extras',
        ),
        migrations.RemoveField(
            model_name='subs',
            name='price_of_extra',
        ),
        migrations.RemoveField(
            model_name='subs',
            name='size',
        ),
        migrations.AlterField(
            model_name='subs',
            name='sub',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Subs_Items'),
        ),
    ]
