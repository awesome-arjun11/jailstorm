from django import template
from blog.models import *
from django.db.models import Count
register = template.Library()
# BlogCategory snippets
@register.inclusion_tag('blog/tags/blog_category_list_page.html', takes_context=True)
def categorylist(context):
  m = BlogCategory.objects.all().count() 
  if m%2 == 0:
    n = m / 2
  else:
    n = (m+1)/2  
 
  return {
    'fcategorylist': BlogCategory.objects.all()[:n],
    'scategorylist': BlogCategory.objects.all()[n:],
    'request': context['request'],
  }