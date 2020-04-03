import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .forms import TodoItemForm
from .models import TodoItem
from .serializers import deserialize, serialize, serialize_many


@csrf_exempt
def todo_item_view(request, item_id):
    """
        Single todo item endpoint.
    """
    
    # Delete selected item
    if request.method == 'DELETE':
        item = TodoItem.objects.get(id=item_id)
        item.delete()
        return HttpResponse(status=204)

    # Update item model with new data.
    elif request.method == 'PUT':
        data = deserialize(request.body)
        item = TodoItem.objects.get(id=data['id'])
        del data['id']
        for key, val in data.items():
            setattr(item, key, val)
        item.save()
        return HttpResponse(status=204)


@csrf_exempt
def todo_items_all_view(request):
    """
        All todo items endpoint.
    """

    # Get all todo items.
    if request.method == 'GET':
        todo_items = TodoItem.objects.all()
        return HttpResponse(serialize_many(todo_items), status=200)

    # Create new todo item.
    if request.method == 'POST':
        form = TodoItemForm(json.loads(request.body))
        if form.is_valid():
            todo_item = TodoItem(title=form.cleaned_data['title'])
            todo_item.save()
            return HttpResponse(serialize(todo_item), status=201)
        return HttpResponse('Submitted data is invalid.', status=400)
