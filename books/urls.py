from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import home, BookListView, BookDetailView


app_name = 'books' 

urlpatterns = [
    path('', home, name='home'),
    path('list/', BookListView.as_view(), name='list'),
    path('list/<pk>', BookDetailView.as_view(), name='detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)