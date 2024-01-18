# dZENcode

<br>

<div align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/django-logo-negative.svg">
  <img alt="Dark and Light mode version of the Django logo" src="./assets/django-logo-positive.svg">
</picture>
</div>

<br>

[![Python Version](https://img.shields.io/badge/Python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![PostgreSQL Version](https://img.shields.io/badge/PostgreSQL-13-green.svg)](https://www.postgresql.org/docs/13/release-13-2.html)
[![Flake8](https://img.shields.io/badge/Flake8-Check%20Code-yellow.svg)](https://flake8.pycqa.org/)
[![Django Simple Captcha Version](https://img.shields.io/badge/Django%20Simple%20Captcha-0.6-orange.svg)](https://django-simple-captcha.readthedocs.io/en/latest/)


## Running the Project Locally

1. Open you terminal and put the command:
```bash
git clone https://github.com/y00tss/dZENcode_test_task.git
```
2. Open Docker Desktop on your Windows

3. Back to your terminal and put the command:
```bash
cd dZENcode_test_task
```
4. Next step is creating the conteiner by following command:
```bash
docker-compose build
```
5. Next command:
```bash
docker-compose run --rm app sh -c "python manage.py makemigrations"
```
6. After we need to create a superuser. Follow the guide inside (username and passwordx2):
```bash
docker-compose run --rm app sh -c "python manage.py createsuperuser"
```
7. Start the server:
```bash
docker-compose up
```
