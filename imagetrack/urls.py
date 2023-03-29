from django.urls import path
from . import views


# Create your urls here.
urlpatterns = [
    path('get_track/<int:pk>', views.GetTrackAPIView.as_view(), name='get_track'),
    path('create_track', views.CreateTrackAPIView.as_view(), name='create_track'),
    path('delete_state/<int:pk>', views.DeleteTrackAPIView.as_view(), name='delete_track'),

]