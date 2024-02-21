from django.urls import path
from .views import login_view, logout_view, main_page, delete_picture, update_description
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('main/', main_page, name='main_page'),
    path('delete/<int:picture_id>/', delete_picture, name='delete_picture'),
    path('update_description/<int:picture_id>/', update_description, name='update_description'),
    # Add more paths as needed
]

if settings.DEBUG:
    urlpatterns += static('/images/', document_root=settings.BASE_DIR / 'images')
