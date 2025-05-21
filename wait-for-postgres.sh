#!/bin/sh

set -e

host="$1"
shift
cmd="$@"

until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$host" -U "contraloria_user" -d "contraloria_db" -c '\q'; do
  >&2 echo "PostgreSQL no está disponible - esperando..."
  sleep 1
done

>&2 echo "PostgreSQL está listo - ejecutando comando"
exec $cmd