from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path
from django.conf.urls.static import static
from codeforces.views import blog, noblog
from accounts.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),

    path('api-auth/', include('rest_framework.urls')),
    path('', home, name='home'),
    path('blog/entry/', noblog, name='noblog'),
    re_path(r'^blog/entry/(?P<pg>\d+)/$', blog, name='blogs'),
    
    path('problemset/', include(('codeforces.urls', 'problemset'), namespace='problemset')),
    path('explo/', include('explo.urls')),
    path('quiz/', include('quiz.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
