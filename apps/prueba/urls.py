from django.urls import path

from .views import IndexView,OtroView

urlpatterns = [
    path('', IndexView.as_view(),name='home'),
    path('otro', OtroView.as_view(),name='otro'),
    
]