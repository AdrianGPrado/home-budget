from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', 'apps.budget.views.index', name='index'),

    url(r'^index.html/$', 'apps.budget.views.index', name='index'),
]
