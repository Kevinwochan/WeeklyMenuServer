# https://github.com/tiangolo/uvicorn-gunicorn-docker/blob/master/docker-images/python3.8.dockerfile (with minor changes)
FROM python:3.8

COPY ./docker-files/requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

COPY ./docker-files/start.bash /start.bash
RUN chmod +x /start.bash

COPY ./docker-files/gunicorn_conf.py /gunicorn_conf.py

COPY ./app /app
WORKDIR /app/

ENV CONTAINER=1
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1
ENV PYTHONIOENCODING=UTF-8

COPY .env /.env

EXPOSE 80

# Run the start script
# And then will start Gunicorn with Uvicorn
CMD ["bash", "/start.bash"]
