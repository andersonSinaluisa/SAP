
from django.conf.urls import url
from django.urls import path


from library.views.library import LibraryCreate, LibraryList,LibraryCompare


urlpatterns = [
    path('create', LibraryCreate.as_view(), name="library"),
    path('list', LibraryList.as_view(), name="library"),
    path('compare', LibraryCompare.as_view(), name="library"),
]