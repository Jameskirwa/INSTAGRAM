from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^accounts/profile/upload/', views.image_upload, name='upload'),
    url(r'accounts/profile/(?P<username>\w+)', views.profile, name='profile'),
    url('profile/', views.homepage, name='home'),
    url(r'^logout/$',auth_views.logout,{"next_page":'/'}),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
