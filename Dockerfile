FROM python:3.9

WORKDIR /app

RUN pip install locust
COPY . .

CMD ["locust", "-f", "locustfile.py", "--host=https://hello-world-test-shub-ws-8080.tfy-ctl-euwe1-devtest.devtest.truefoundry.tech"]
