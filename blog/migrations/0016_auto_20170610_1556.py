# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-10 10:26
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtaildocs.blocks
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20170608_2059'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogcategory',
            options={'verbose_name_plural': 'blog category'},
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('two_columns', wagtail.wagtailcore.blocks.StructBlock((('background', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('bg-warning', 'red'), ('', 'white'), ('bg-primary', 'blue'), ('bg-success', 'green')])), ('left_column', wagtail.wagtailcore.blocks.StreamBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('embedded_video', wagtail.wagtailembeds.blocks.EmbedBlock()), ('google_map', wagtail.wagtailcore.blocks.StructBlock((('map_long', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), ('map_lat', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), ('map_zoom_level', wagtail.wagtailcore.blocks.CharBlock(default=14, max_length=3, required=True))))), ('URL', wagtail.wagtailcore.blocks.URLBlock()), ('PageChooser', wagtail.wagtailcore.blocks.PageChooserBlock()), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock())), icon='arrow-left', label='Left column content')), ('right_column', wagtail.wagtailcore.blocks.StreamBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('embedded_video', wagtail.wagtailembeds.blocks.EmbedBlock()), ('google_map', wagtail.wagtailcore.blocks.StructBlock((('map_long', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), ('map_lat', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), ('map_zoom_level', wagtail.wagtailcore.blocks.CharBlock(default=14, max_length=3, required=True))))), ('URL', wagtail.wagtailcore.blocks.URLBlock()), ('PageChooser', wagtail.wagtailcore.blocks.PageChooserBlock()), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock())), icon='arrow-right', label='Right column content'))))), ('embedded_video', wagtail.wagtailembeds.blocks.EmbedBlock(icon='media')), ('google_map', wagtail.wagtailcore.blocks.StructBlock((('map_long', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), ('map_lat', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), ('map_zoom_level', wagtail.wagtailcore.blocks.CharBlock(default=14, max_length=3, required=True))))), ('URL', wagtail.wagtailcore.blocks.URLBlock()), ('PageChooser', wagtail.wagtailcore.blocks.PageChooserBlock()), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock()))),
        ),
    ]
