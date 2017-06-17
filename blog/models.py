from django.db import models
from django import forms
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from wagtail.utils.pagination import paginate
# Create your models here.
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailsearch import index
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtaildocs.blocks import DocumentChooserBlock
from wagtail.wagtailadmin.edit_handlers import FieldPanel, FieldRowPanel,MultiFieldPanel, InlinePanel, PageChooserPanel, StreamFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.tags import ClusterTaggableManager
from taggit.models import TaggedItemBase
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailcore.blocks import URLBlock, PageChooserBlock, RawHTMLBlock



class GoogleMapBlock(blocks.StructBlock):
    map_long = blocks.CharBlock(required=True,max_length=255)
    map_lat = blocks.CharBlock(required=True,max_length=255)
    map_zoom_level = blocks.CharBlock(default=14,required=True,max_length=3)
 
    class Meta:
        template = 'blog/google_map_block.html'
        icon = 'cogs'
        label = 'Google Map'


class TwoColumnBlock(blocks.StructBlock):
    COLOUR_CHOICES = (
        ('bg-warning', 'red'),
        ('', 'white'),
        ('bg-primary', 'blue'),
		('bg-success', 'green'),
    )
    background = blocks.ChoiceBlock(choices=COLOUR_CHOICES,default="white")
    left_column = blocks.StreamBlock([
            ('heading', blocks.CharBlock(classname="full title")),
            ('paragraph', blocks.RichTextBlock()),
            ('image', ImageChooserBlock()),
            ('embedded_video', EmbedBlock()),
            ('google_map', GoogleMapBlock()),
            ('URL',URLBlock()),			 
            ('PageChooser',PageChooserBlock()),
            ('document',DocumentChooserBlock()),
        ], icon='arrow-left', label='Left column content')
 
    right_column = blocks.StreamBlock([
            ('heading', blocks.CharBlock(classname="full title")),
            ('paragraph', blocks.RichTextBlock()),
            ('image', ImageChooserBlock()),
            ('embedded_video', EmbedBlock()),
            ('google_map', GoogleMapBlock()),
            ('URL',URLBlock()),
            ('PageChooser',PageChooserBlock()),
            ('document',DocumentChooserBlock()),
        ], icon='arrow-right', label='Right column content')
 
    class Meta:
        template = 'blog/two_column_block.html'
        icon = 'placeholder'
        label = 'Two Columns'




class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]
	#include published content only .In chronological order..
	
    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super(BlogIndexPage, self).get_context(request)
        blogpages_list = self.get_children().live().order_by('-first_published_at')
        page = request.GET.get('page', 1)
        paginator = Paginator(blogpages_list, 5)
        try:
            blogpages = paginator.page(page)
        except PageNotAnInteger:
            blogpages = paginator.page(1)
        except EmptyPage:
            blogpages = paginator.page(paginator.num_pages)
		
        context = {'blogpages' : blogpages}
        return context


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey('BlogPage', related_name='tagged_items')
		
		
# Blog post
class BlogPage(Page):
    author = ParentalManyToManyField('blog.BlogAuthor')
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title", icon="title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock(icon="image")),
	    ('two_columns', TwoColumnBlock()),
        ('embedded_video', EmbedBlock(icon="media")),
        ('google_map', GoogleMapBlock()),
		('URL',URLBlock()),
		('PageChooser',PageChooserBlock()),
		('document',DocumentChooserBlock()),
        ('table',RawHTMLBlock()),

    ])
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    categories = ParentalManyToManyField('blog.BlogCategory', blank=True)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None


    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
		index.SearchField('author',partial_match=True),



    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
		    FieldPanel('author', widget=forms.CheckboxSelectMultiple),
            FieldPanel('date'),
            FieldPanel('tags'),
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        ], heading="Blog information"),
        FieldPanel('intro'),
        StreamFieldPanel('body'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]
	
	
	
	
class BlogPageGalleryImage(Orderable):
    page = ParentalKey(BlogPage, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]
	
class BlogTagIndexPage(Page):

    def get_context(self, request):

        # Filter by tag
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)

        # Update template context
        context = super(BlogTagIndexPage, self).get_context(request)
        context['blogpages'] = blogpages
        return context
		
		
		
@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )
	
    search_fields= Page.search_fields + [
        index.SearchField('name'),
	
	]

    panels = [
        FieldPanel('name'),
        ImageChooserPanel('icon'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'blog category'
		
		

class BlogCategoryIndexPage(Page):

    def get_context(self, request):

        # Filter by categories
        category = request.GET.get('category')
        blogpages = BlogPage.objects.filter(categories__name=category)

        # Update template context
        context = super(BlogCategoryIndexPage, self).get_context(request)
        context['blogpages'] = blogpages
        return context

	
	
		
@register_snippet
class BlogAuthor(models.Model):
    name = models.CharField(max_length=150, blank=False)
    description = models.CharField(max_length=255)

    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

	
    search_fields= Page.search_fields + [
        index.SearchField('name'),
	
	]

    panels = [
        FieldPanel('name'),
        FieldPanel('description'),
        ImageChooserPanel('icon'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'blog authors'
		
		
class BlogAuthorIndexPage(Page):

    def get_context(self, request):

        # Filter by tag
        authors = request.GET.get('authors')
        blogpages = BlogPage.objects.filter(author__name=authors)
        blogger = BlogAuthor.objects.get(name=authors)
        # Update template context
        context = super(BlogAuthorIndexPage, self).get_context(request)
        context = {'blogpages' : blogpages,
		'blogger' : blogger }
        return context

