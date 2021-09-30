import json

from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, FormView
from django.http import HttpResponse

from .models import Contact
from .forms import ContactForm


class HomeView(TemplateView):

    template_name = 'home.html'


class SearchView(TemplateView):

    template_name = 'search.html'


class AboutUsView(TemplateView):
    
    template_name = 'about/about.html'


class AboutOfficeView(TemplateView):
    
    template_name = 'about/about-office.html'


class AboutOfficePageView(TemplateView):
    
    template_name = 'about/about-office-page.html'


class ListPropertyView(TemplateView):
    
    template_name = 'list/listyourproperty_empty.html'


class ListNewPropertyView(TemplateView):
    
    template_name = 'list/listyourproperty.html'


class NewsblogView(TemplateView):
    
    template_name = 'news/newsblog.html'


class NewsOpenView(TemplateView):
    
    template_name = 'news/newsblog__open.html'


class PropertyView(TemplateView):
    
    template_name = 'property/property.html'


class AgentPageView(TemplateView):
    
    template_name = 'agent/agentpage.html'


class Form1View(TemplateView):
    
    template_name = 'forms/form1.html'


class FormUser1View(TemplateView):
    template_name = 'forms/form_user1.html'


class FormUser1View(TemplateView):
    
    template_name = 'search.html'


class ContactCreate(FormView):
    model = Contact
    form_class = ContactForm
    success_url = "/"
    template_name = None

    def form_valid(self, form):
        form.save()
        return HttpResponse(json.dumps({'ok': 200}))

    def form_invalid(self, form):
        data = []
        for k, v in form._errors.items():
            text = {
                'desc': ', '.join(v),
            }
            if k == '__all__':
                text['key'] = '#%s' % self.request.POST.get('form')
            else:
                text['key'] = '#id_%s' % k
            data.append(text)
        return HttpResponse(json.dumps(data))
