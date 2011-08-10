'''
Created on 08/03/2011

@author: Jhoni
'''

from sonora_portal001 import settings

def metas(request):
    return {
        u'site_name': settings.SITE_NAME,
        u'meta_keywords': settings.META_KEYWORDS,
        u'meta_description': settings.META_DESCRIPTION,
        u'request': request
}

def login(request):
    if 'next' in request.GET:
        return { 'NEXT': request.GET['next'] }
    else:
        return { 'NEXT': request.path }