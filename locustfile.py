from locust import HttpUser, task, between
import random

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)  # Wait time between tasks

    @task
    def hit(self):
        if random.choice([True, False]):
            self.client.get("/ping")
        else:
            self.client.get("/uuid")