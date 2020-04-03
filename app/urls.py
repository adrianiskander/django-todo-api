from django.urls import include, path


urlpatterns = [
    path('api/todo/', include('app.todo.urls'))
]
