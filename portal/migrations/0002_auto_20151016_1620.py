# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_title', models.TextField()),
                ('product_type', models.TextField()),
                ('product_link', models.TextField()),
                ('product_image', models.ImageField(upload_to=b'product_images', blank=True)),
                ('product_price', models.TextField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='ItemsBought',
            field=models.ManyToManyField(to='portal.Products'),
        ),
    ]
