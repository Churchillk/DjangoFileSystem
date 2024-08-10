from django.urls import path
from . import views as HomeViews

urlpatterns = [
    path("", HomeViews.main, name="home"),
]
