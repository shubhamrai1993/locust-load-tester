FROM python:3.9

WORKDIR /app

RUN pip install locust
COPY . .

CMD ["locust", "-f", "locustfile.py"]
