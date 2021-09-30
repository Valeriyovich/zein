"""zain_property URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from property.views import HomeView, ContactCreate, AboutUsView,AgentPageView, SearchView, AboutOfficeView,PropertyView, AboutOfficePageView,FormUser1View,NewsblogView,NewsOpenView,Form1View, FormUser1View, ListPropertyView, ListNewPropertyView
from users.views import AjaxLoginView, AjaxSignUpView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('accounts/', include('allauth.urls')),
    path('ajax/login/', AjaxLoginView.as_view(), name='ajax_login'),
    path('ajax/signup/', AjaxSignUpView.as_view(), name='ajax_signup'),
    path('contact_create/', ContactCreate.as_view(), name='contact_create'),
    path('about/', AboutUsView.as_view(), name='about'),
    path('about_office/', AboutOfficeView.as_view(), name='about_office'),
    path('about_office_page/', AboutOfficePageView.as_view(), name='about_office_page'),
    path('property/list/', ListPropertyView.as_view(), name='list_property'),
    path('property/list/new/', ListNewPropertyView.as_view(), name='list_new_property'),
    path('search/', SearchView.as_view(), name='search'),
    path('news_blog/', NewsblogView.as_view(), name='news_blog'),
    path('news_blog/open/', NewsOpenView.as_view(), name='news_blog_open'),
    path('form1/', Form1View.as_view(), name='form1'),
    path('form_user/', FormUser1View.as_view(), name='formuser1'),
    path('property/', PropertyView.as_view(), name='property'),
    path('agentpage/', AgentPageView.as_view(), name='agentpage'),
    path('myaccount/', FormUser1View.as_view(), name='form_user1')
]
