from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from server import views
from server.UserView import SuperHeroView, FilterSuperHeroView

admin.autodiscover()

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^superheros/$', SuperHeroView.as_view()),
    url(r'^superheros/(?P<superhero_id>[\w-]+)/$', SuperHeroView.as_view()),
    url(r'^findsuperhero/$',FilterSuperHeroView.as_view())



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
