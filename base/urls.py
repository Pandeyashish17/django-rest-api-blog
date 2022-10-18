from django.urls import path
from . import views
urlpatterns = [
    path("",views.home),
    path("articles/",views.articles),
    path("authors/",views.authors)
]
