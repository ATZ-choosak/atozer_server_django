from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.models import *


@api_view(['GET'])
def TaskDayViewsetAll(request):
    if request.method == "GET":
        task = []
        if Task_day.objects.all().count() > 0:
            for i in Task_day.objects.all():
                task.append({
                    "id": i.id,
                    "users": {"id": i.users.id, "name": i.users.name},
                    "status": i.status,
                    "date": i.date
                })
        return Response({"data": task})

    if request.method == "POST":

        user = request.data['user']
        date = request.data['date']

        new_task = Task_day.objects.create()
        new_task.users = Player.objects.get(id=user)
        new_task.date = date
        new_task.save()

        print(user, date)

        return Response({"Added Task Day."})


@api_view(['GET', 'POST'])
def TaskDayViewsetOne(request):
    if request.method == "GET":
        task = {}
        if Task_day.objects.all().count() > 0:
            data = Task_day.objects.last()
            task = {
                "id": data.id,
                "users": {"id": data.users.id, "name": data.users.name},
                "status": data.status,
                "date": data.date
            }

        return Response({"data": task})

    if request.method == "POST":

        user = request.data['user']
        date = request.data['date']

        new_task = Task_day.objects.create()
        new_task.users = Player.objects.get(id=user)
        new_task.date = date
        new_task.save()

        print(user, date)

        return Response({"Added Task Day."})

    if request.method == "DELETE":
        id = request.params.id

        print(id)

        return Response({"Added Task Day."})
