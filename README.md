
# y00tss

<br>

<div align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/django-logo-negative.svg">
  <img alt="Dark and Light mode version of the Django logo" src="./assets/django-logo-positive.svg">
</picture>
</div>

<br>

[![Python Version](https://img.shields.io/badge/Python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![Django Version](https://img.shields.io/badge/Django-4.2-blue.svg)](https://docs.djangoproject.com/en/4.2/releases/4.2/)
[![PostgreSQL Version](https://img.shields.io/badge/PostgreSQL-13-green.svg)](https://www.postgresql.org/docs/13/release-13-2.html)
[![Flake8](https://img.shields.io/badge/Flake8-Check%20Code-yellow.svg)](https://flake8.pycqa.org/)
[![Django Simple Captcha Version](https://img.shields.io/badge/Django%20Simple%20Captcha-0.6-orange.svg)](https://django-simple-captcha.readthedocs.io/en/latest/)
[![django-mptt Version](https://img.shields.io/badge/django--mptt-0.12.0-brightgreen.svg)](https://django-mptt.readthedocs.io/en/latest/)
[![tzlocal Version](https://img.shields.io/badge/tzlocal-5.0-yellowgreen.svg)](https://tzlocal.readthedocs.io/en/latest/)


## Running the Project Locally

1. Open you terminal and put the command:
```bash
git clone https://github.com/y00tss/Comment-system
```
2. Open Docker Desktop on your Windows

3. Back to your terminal and put the command:
```bash
cd Comment-system
```
4. Next step is creating the conteiner by following command:
```bash
docker-compose build
```
6. After we need to create a superuser. Follow the guide inside (username and passwordx2) or you can follow next step if you don`t want to visit Django Admin:
```bash
docker-compose run --rm app sh -c "python manage.py createsuperuser"
```
7. Start the server:
```bash
docker-compose up
```
8. Open the link:
<a href="http://127.0.0.1:8000/" target="_blank">WebApp</a>

# Settings
1. Database local, default PORT = 5432 , keep this port free before Running App
2. Nested reply is limited. Follow to src/comment/service/comment_settings.py and change MAX_NODE_LEVEL
3. Prepare your eyes. I found a bad template, so nested comments looks a little strange



