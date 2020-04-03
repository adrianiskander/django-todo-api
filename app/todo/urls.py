from django.urls import path
from . import views


urlpatterns = [
    path('', views.todo_items_all_view),
    path('<item_id>', views.todo_item_view)
]
