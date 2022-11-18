call cd ..
call environment\Scripts\activate
call cd atozer_server_django
call python manage.py makemigrations users
call python manage.py makemigrations task_day
call python manage.py makemigrations task_week
call python manage.py migrate