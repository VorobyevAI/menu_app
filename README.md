git clone 
cd django_menu
python3 -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
cd menu_project
python manage.py makemigrations
python manage.py migrate
python manage.py runserver