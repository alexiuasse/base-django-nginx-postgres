#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
      echo "Waiting for postgres... $DATABASE_HOST $DATABASE_PORT"
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# python manage.py flush --no-input
python manage.py collectstatic
# python manage.py makemigrations
python manage.py migrate

exec "$@"
