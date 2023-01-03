FROM python:3.10

RUN apt-get update && \
    apt-get install -y && \
    python3 -m pip install --upgrade pip && \
    pip3 install daphne 

COPY . /opt/COMICBOOK-CHARACTERS
WORKDIR /opt/COMICBOOK-CHARACTERS
RUN pip3 install -r /opt/COMICBOOK-CHARACTERS/requirements.txt
RUN pip3 install psycopg2
WORKDIR /opt/COMICBOOK-CHARACTERS/my_site
RUN python3 manage.py collectstatic
RUN apt-get update && apt-get install -y redis-server
EXPOSE 9190

CMD ["gunicorn", "-b", "0.0.0.0:9190", "my_site.asgi:application"]