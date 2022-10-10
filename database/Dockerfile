# pull official base image
FROM postgres:13.0-alpine

# set work directory
WORKDIR /usr/src/app

# install postgres dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

ENV TZ=America/Sao_Paulo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# copy project
COPY . .