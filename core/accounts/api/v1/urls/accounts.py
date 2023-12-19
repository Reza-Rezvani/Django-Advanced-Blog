from django.urls import include, path
from .. import views
# from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    # registration
    path('registration/', views.RegistrationApiView.as_view(), name='registration'),
    
    # activation

    # resend activation
    
    # change password
    path('change-password', views.ChangePasswordApiView.as_view(), name='change-password'),
    
    # reset password

    # login token
    path('token/login', views.CustomObtainAuthToken.as_view(), name='token-login'),
    path('token/logout', views.CustomDiscardAuthToken.as_view(), name='token-logout'),

    # login jwt
    path('jwt/create/', views.CustomTokenObtainPairView.as_view(), name='token-create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='token-verify'),

]