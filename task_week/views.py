from rest_framework.decorators import api_view
from .models import *
from users.views import *
from rest_framework.response import Response


@api_view(['GET'])
def task_week_all(request):
    if request.method == "GET":
        data = Task_week.objects.all()
        task = []
        if data.count() > 0:
            for i in data:
                task.append(
                    {
                        "users": [{"id": a.id, "name": a.name} for a in i.users.all()],
                        "status_1": i.status_1,
                        "status_2": i.status_2,
                        "date": i.date
                    }
                )
        return Response({'data': task})


@api_view(['GET', 'POST'])
def task_week(request):
    if request.method == "GET":
        data = Task_week.objects.all()
        task = {}
        if data.count() > 0:
            task = {
                "users": [{"id": a.id, "name": a.name} for a in data.last().users.all()],
                "status_1": data.last().status_1,
                "status_2": data.last().status_2,
                "date": data.last().date
            }
        return Response({'data': task})

    if request.method == "POST":

        users = request.data['users']
        date = request.data['date']

        task_new = Task_week.objects.create()
        user_lst = [Player.objects.get(
            id=users[0]), Player.objects.get(id=users[1])]
        task_new.users.set(user_lst)
        task_new.date = date
        task_new.save()

        return Response({'data': 'Added Task Week.'})
