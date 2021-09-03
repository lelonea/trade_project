FROM python:3.8-slim
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /app
COPY Pipfile Pipfile.lock /app/


RUN pip install pipenv \
    && pipenv install --deploy --system --ignore-pipfile

COPY . /app/
RUN chmod +x entrypoint.sh

CMD ./entrypoint.sh
