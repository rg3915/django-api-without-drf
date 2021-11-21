# Django API without DRF

This is a API project made with Django, and without Django REST framework.

## This project was done with:

* [Python 3.9.8](https://www.python.org/)
* [Django 3.2.9](https://www.djangoproject.com/)

## How to run project?

* Clone this repository.
* Create virtualenv with Python 3.
* Active the virtualenv.
* Install dependences.
* Run the migrations.

```
git clone https://github.com/rg3915/django-api-without-drf.git
cd django-api-without-drf
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
python manage.py createsuperuser --username="admin" --email=""
```

## endpoints

```
/api/v1/videos/                 backend.core.views.video_list   core:video_list
/api/v1/videos/<int:pk>/        backend.core.views.video_detail core:video_detail
/api/v1/videos/<int:pk>/delete/ backend.core.views.video_delete core:video_delete
/api/v1/videos/<int:pk>/update/ backend.core.views.video_update core:video_update
/api/v1/videos/create/          backend.core.views.video_create core:video_create
/api/v2/videos/                 backend.core.views.videos       core:videos
/api/v2/videos/<int:pk>/        backend.core.views.video        core:video
```

## Examples with httpie

TODO

## TDD

TODO
