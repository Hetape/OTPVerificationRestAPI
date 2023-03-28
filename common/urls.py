from django.urls import path
from . import views



# Create your urls here.
urlpatterns = [
    path('get_state', views.GetStateAPIView.as_view(), name='get_state'),
    path('create_state', views.CreateStateAPIView.as_view(), name='create_state'),
    path('delete_state/<int:pk>', views.DeleteStateAPIView.as_view(), name='delete_state'),
    path('get_city', views.GetCityAPIView.as_view(), name='get_city'),
    path('create_city', views.CreateCityAPIView.as_view(), name='create_city'),
    path('delete_city/<int:pk>', views.DeleteCityAPIView.as_view(), name='delete_city'),
    path('get_area', views.GetAreaAPIView.as_view(), name='get_area'),
    path('create_area', views.CreateAreaAPIView.as_view(), name='create_area'),
    path('delete_area/<int:pk>', views.DeleteAreaAPIView.as_view(), name='delete_area'),

]