from django.urls import path
from . import views
urlpatterns = [
    path("",views.home),
    path("articles/",views.articles),
    path("articles/<str:pk>/",views.singleArticles),
    path("authors/",views.authors),
    path("categories/",views.authors),
    path("tags/",views.tags)
]
