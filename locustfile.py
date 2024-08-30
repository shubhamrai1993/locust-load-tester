from locust import HttpUser, task, between
import random

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)  # Wait time between tasks

    @task
    def hit(self):
        self.client.get("/status/200")
    
    @task(3)
    def fail(self):
        self.client.get("/status/500")