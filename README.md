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


   Installation
------------

Required
~~~~~~~~
#. Open you terminal and put the command
   ::

        git clone https://github.com/y00tss/dZENcode_test_task.git

#. Open Docker Desktop on your Windows

#. Back to your terminal and put the command
   ::

        cd dZENcode_test_task

#. Next step is creating the conteiner by following command
   ::

        docker-compose build

#. Next command
   ::

        docker-compose run --rm app sh -c "python manage.py makemigrations"

#. After we need to create a superuser. Follow the guide inside (username and passwordx2)
   ::

        docker-compose run --rm app sh -c "python manage.py createsuperuser"

#. Start the server
   ::

        docker-compose up
