from django.urls import path, include
from todo.views import get_all_active_todos, create_new_todo, update_todo

urlpatterns = [
    path('todos/active', get_all_active_todos),
    path('todo/create', create_new_todo),
    path('todo/<id>', update_todo),

]
