from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^law_and_order/', include('law_and_order.urls')),
    url(r'^$', TemplateView.as_view(template_name='law_and_order/home.html'), name='home'),

]

