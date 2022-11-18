call cd ..
call environment_server\Scripts\activate
call cd atozer_server_django
call python manage.py runserver 0.0.0.0:8000
pause