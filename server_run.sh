#!/bin/bash
# CRIO_SOLUTION_AND_STUB_START_MODULE_BASIC
# This script must contain a series of commands to run the backend application

# # Eg:- For Python Flask Project
#         export FLASK_APP=main.py
#         flask run

# CRIO_SOLUTION_AND_STUB_END_MODULE_BASIC
cd xharktank
# cmd = "python manage.py makemigrations"
# os.system(cmd)
# cmd = "python manage.py migrate"
# os.system(cmd)
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 8081
