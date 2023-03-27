FROM python:3.9-alpine
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /code/

ENV DOCKERIZED=1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "thaifishid.wsgi:application"]

# After each build, run:
# docker exec -it <container_id> python manage.py makemigrations
# docker exec -it <container_id> python manage.py migrate
