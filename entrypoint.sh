echo "Running entrypoint.sh"
sleep 15
python manage.py test iban_crud/tests
python manage.py makemigrations
python manage.py migrate
python manage.py shell < initial_model_setup.py
python manage.py runserver 0.0.0.0:8000