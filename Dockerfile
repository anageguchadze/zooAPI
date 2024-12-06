FROM python:alpine

WORKDIR /app

COPY . .

CMD [ "python", "hello.py" ]