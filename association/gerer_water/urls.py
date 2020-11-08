from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views
urlpatterns = [

    path('', views.saison_form),
    path('saison/', views.saison_list),

]

