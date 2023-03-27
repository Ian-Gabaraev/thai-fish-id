FROM python:3.9-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV DOCKERIZED=1

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# After each build, run:
# docker exec -it <container_id> python manage.py makemigrations
# docker exec -it <container_id> python manage.py migrate