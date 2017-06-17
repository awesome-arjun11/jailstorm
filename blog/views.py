from django.shortcuts import render
from django.views import generic
from blog.models import BlogAuthor , BlogCategory
from django.http import HttpResponse, HttpResponseRedirect
# new imports that go at the top of the file
from django.core.mail import EmailMessage
from django.contrib import messages

from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template
from .forms import ContactForm
# Create your views here.

def about(request):
    team_members = BlogAuthor.objects.all()
    context = {'team_members' : team_members}
    return render(request,'blog/about.html',context) 

	
'''#class CategoryListView(generic.ListView):
    #template_name = 'blog/blog_category_list_page.html'
	
    #def get_queryset(self):
        #return BlogCategory.objects.all()'''
		
		
def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            contact_number = request.POST.get(
            'contact_number'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the 
            # contact information
            template = get_template('blog/contact_template.txt')
            context = dict({
                'contact_name': contact_name,
				'contact_number': contact_number,
                'contact_email': contact_email,
                'form_content': form_content,
            })
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['hbknjr@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            messages.success(request, 'Form submission successful')
            return redirect('contact')

    return render(request, 'blog/contact.html', {'form': form_class})