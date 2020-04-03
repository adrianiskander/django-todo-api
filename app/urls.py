from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.home_view),
    path('api/todo/', include('app.todo.urls'))
]
