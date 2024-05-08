from django.contrib import admin
from django.urls import path

from main.views import (
    AuthorAPIList, AuthorAPIUpdate, AuthorPIDestroy, AuthorViewSet, 
    BookAPIList, BookAPIUpdate, BookPIDestroy, BookViewSet
)

urlpatterns = [
    path("admin/", admin.site.urls),
    
    path("v1/author/", AuthorAPIList.as_view()),
    path("v1/author/<int:pk>/", AuthorAPIUpdate.as_view()),
    path("v1/authordelete/<int:pk>/", AuthorPIDestroy.as_view()),
    path('v1/author/search/', AuthorViewSet.as_view({'get': 'list'})),
    
    path("v1/book/", BookAPIList.as_view()),
    path("v1/book/<int:pk>/", BookAPIUpdate.as_view()),
    path("v1/bookdelete/<int:pk>/", BookPIDestroy.as_view()),
    path('v1/book/search/', BookViewSet.as_view({'get': 'list'})),
]

