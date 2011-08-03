'''
Created on 14/07/2011

@author: Jhoni
'''
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('portfolio.views',
          
        url(r'^$', 'portfolios', 
            {'template_name':'portfolio/portfolios.html'}, name='portfolios'),
                  
        url(r'^(?P<portfolio_slug>[-\w]+)/$', 'portfolio', 
            {'template_name':'portfolio/portfolio.html'}, name='portfolio'),
        )