sleep 5; 
python3 ./manage.py makemigrations --noinput;
python3 ./manage.py migrate --noinput;
python3 ./manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('dev', 'dev@dev.com', 'dev')"
python3 ./manage.py runserver 0.0.0.0:8000;