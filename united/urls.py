from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path
from django.conf.urls.static import static
from codeforces.views import blog, noblog

urlpatterns = [
    path('blog/entry/', noblog, name='noblog'),
    re_path(r'^blog/entry/(?P<pg>\d+)/$', blog, name='blogs'),
    path('problemset/', include(('codeforces.urls', 'problemset'), namespace='problemset')),
    path('explo/', include(('explo.urls', 'explo'), namespace='explo')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
