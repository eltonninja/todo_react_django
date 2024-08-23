from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import TodoForm
from .models import Todo


def get_all_active_todos(request):
    todos = Todo.objects.filter(completed=False).order_by("-id").values('id', 'title', 'completed')
    return JsonResponse(data=list(todos), safe=False)


@csrf_exempt
def create_new_todo(requests):
    if requests.method == "POST":
        todo = TodoForm(data=requests.POST)
        if todo.is_valid():
            todo_obj = Todo(title=todo.cleaned_data.get("title"))
            todo_obj.save()
            return JsonResponse(data={"message": "Todo added successfully"})
        else:
            return JsonResponse(data=todo.errors, status=400)

    return JsonResponse(data={"message": "Unable to verify request"}, status=403)


@csrf_exempt
def update_todo(request, id):
    if request.method == "PATCH":
        try:
            todo = Todo.objects.get(id=id)
            todo.completed = True
            todo.save()
            return JsonResponse(data={"message": "Todo updated successfully"})
        except Todo.DoesNotExist:
            return JsonResponse(data="Todo object does not exist", status=400)

    return JsonResponse(data={"message": "Unable to verify request"}, status=403)