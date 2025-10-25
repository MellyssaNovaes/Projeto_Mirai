
FROM python:3.11-slim

WORKDIR /code

COPY . .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["fastapi", "run", "app", "--port", "8000"]
