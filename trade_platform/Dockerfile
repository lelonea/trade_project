FROM python:3.8-slim
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY Pipfile* /app/

RUN pip install pipenv \
    && pipenv install --deploy --system --ignore-pipfile

COPY entrypoint.sh /app/
RUN chmod 755 +x entrypoint.sh
COPY . /app/

CMD ./entrypoint.sh
