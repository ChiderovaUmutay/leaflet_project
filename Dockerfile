FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip3 install --upgrade pip
RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y gdal-bin
RUN export GDAL_LIBRARY_PATH=/home/user:$GDAL_LIBRARY_PATH

COPY . /app/

CMD python manage.py runserver 0.0.0.0:8008

