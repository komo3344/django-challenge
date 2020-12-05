from django.urls import path
from . import views
app_name = 'reviews'

urlpatterns = [
    path('<int:pk>/', views.review_add, name='add'),
    path('remove/<int:pk>/', views.review_remove, name='remove')
]