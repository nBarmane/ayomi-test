FROM python:3.7-alpine

COPY . /home/code/
WORKDIR /home/code

RUN python -m pip install Django \
    && pip install djangorestframework \
    && python manage.py migrate \
    && python manage.py shell < apps/user/utils/insert_user.py

EXPOSE 8002

CMD ["python", "manage.py", "runserver", "0.0.0.0:8002"]