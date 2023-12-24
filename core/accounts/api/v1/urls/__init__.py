from django.urls import include, path
# from .. import views


urlpatterns = [
    path("", include("accounts.api.v1.urls.accounts")),
    path("profile/", include("accounts.api.v1.urls.profiles")),
]
