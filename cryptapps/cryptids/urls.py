from django.urls import path

from . import views

from django.urls import path

from . import views

app_name = 'cryptids'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:cryptid_id>/', views.detail, name='detail'),
]

# Here is all the urls used by the app
