# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-05 05:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20170604_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='author',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()))),
        ),
    ]
