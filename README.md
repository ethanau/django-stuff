# Some demos for learning Django
## [first project](first_project)<br>
- **Veiws**
- URL Mapping
- **Templates**
- Static Files
- **Models**
- Dynamic Response

## [second project](second_project)<br>
- activate virtual environment
- django-admin startproject second_project
- cd second_project
- python manage.py startapp my_app
- add my_app in setting.py
- add models in models.py
- create views and templates
- create urls.py in my_app
- set urls.py in second_project
- register models in admin.py
- python manage.py migrate
- python manage.py makemigrations my_app
- python manage.py createsuperuser

## [third project](third_project)<br>
- create forms.py
- connect form and model
- add user sign up function in second project

## [fourth project](fourth_project)<br>
- relative URLs with templates
- URL template inheritance
- template filter
- custom filter

## [fifth project](fifth_project)<br>
- static folder(website side files)
- media folder(user side files, like user profile)
- User model
- connect models and forms
- registration and login functionality

## [CBVs project](cbv_project)<br>
- template views with CBV
- list view
- detail view