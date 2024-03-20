from django.contrib import admin
from django.urls import path, include
from home import views as home_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('credits/', home_views.credits, name="credits"),
    path('about/', home_views.about, name="about"),
    path('version/', home_views.version, name="version"),
    path('news/', home_views.news, name="news"),
    path('news_advanced/', home_views.news_advanced, name="news_advanced"),
    path('bands/', include("bands.urls")),
]
