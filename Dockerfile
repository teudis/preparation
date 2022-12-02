FROM python:3.9.6-alpine

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /code

# install dependencies
RUN apk add --update --no-cache postgresql-client jpeg-dev && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev zlib zlib-dev linux-headers && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Define logs so they can be persisted between restarts if desirable
VOLUME /var/log/nginx


# copy project
COPY . /code/ 


USER django-user
ENV PATH="/py/bin:$PATH"
