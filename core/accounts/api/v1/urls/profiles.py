from django.urls import include, path
from .. import views



urlpatterns = [

    path('', views.ProfileApiView.as_view(), name='profile'),

]