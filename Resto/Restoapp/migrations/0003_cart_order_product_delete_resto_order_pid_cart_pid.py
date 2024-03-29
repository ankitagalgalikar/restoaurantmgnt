# Generated by Django 5.0 on 2024-01-06 09:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restoapp', '0002_rename_task_resto'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=1)),
                ('cprice', models.FloatField()),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=50)),
                ('qty', models.IntegerField(default=1)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Product_Name')),
                ('price', models.FloatField()),
                ('detail', models.CharField(max_length=100, verbose_name='Product_Detail')),
                ('cat', models.IntegerField(choices=[(1, 'clothes'), (2, 'Mobile'), (3, 'Shoes')], verbose_name='Category')),
                ('is_active', models.BooleanField(default=True)),
                ('pimage', models.ImageField(upload_to='image')),
            ],
        ),
        migrations.DeleteModel(
            name='Resto',
        ),
        migrations.AddField(
            model_name='order',
            name='pid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Restoapp.product'),
        ),
        migrations.AddField(
            model_name='cart',
            name='pid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Restoapp.product'),
        ),
    ]
