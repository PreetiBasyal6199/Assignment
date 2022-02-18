
from django.urls import path
from .views import LoginView,import_data
urlpatterns = [
    path('',LoginView),
    path('import',import_data,name='import'),
]
