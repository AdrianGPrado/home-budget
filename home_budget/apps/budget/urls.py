from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', 'apps.budget.views.index', name=''),

    url(r'index.html/$', 'apps.budget.views.index', name='index'),

    url(r'index-rtl.html$', 'apps.budget.views.index_rtl', name='index'),

    url(r'charts.html$', 'apps.budget.views.charts', name='charts'),

    url(r'tables.html$', 'apps.budget.views.tables', name='tables'),

    url(r'forms.html$', 'apps.budget.views.forms', name='forms'),

    url(r'bootstrap-elements.html$', \
         'apps.budget.views.bootstrap_elements', \
         name='bootstrap-elements'),

    url(r'bootstrap-grid.html$', \
         'apps.budget.views.bootstrap_grid', \
         name='bootstrap-grid'),

    url(r'blank-page.html$', \
         'apps.budget.views.blank_page', \
         name='blank-page'),

]
