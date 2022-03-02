from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static, serve
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view


patterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls', namespace='user')),
    path('journal/', include('travel_journal.urls', namespace='travel_journal')),
]

extrapatterns = [
    # api docs
    path('openapi', get_schema_view(title='Journey Journal API', 
                                    description='Journey Journal is easy way to document travel experiences ', version='1.0.0'), name='openapi'),

    path('docs/', TemplateView.as_view(template_name='api-doc.html',
         extra_context={'schema_url': 'openapi'})),

    path('redoc/', TemplateView.as_view(template_name='redoc.html',
         extra_context={'schema_url': 'openapi'})),
]


if settings.DEBUG:
    staticpatterns = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    staticpatterns = [
        re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
        re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    ]

urlpatterns = patterns + staticpatterns + extrapatterns
