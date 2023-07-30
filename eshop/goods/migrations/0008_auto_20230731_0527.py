# Generated by Django 3.2 on 2023-07-31 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0007_auto_20180201_1637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='goods_desc',
        ),
        migrations.AlterField(
            model_name='goodscategorybrand',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brands', to='goods.goodscategory', verbose_name='商品类目'),
        ),
    ]
