FROM python:3.12

COPY . /app

WORKDIR /app

RUN pip install poetry

RUN poetry config virtualenvs.create false \
    && poetry install

EXPOSE 5000

CMD ["python", "flask-api/app/app.py"]