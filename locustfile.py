from locust import HttpUser, between, task
class UserBehavior(HttpUser):
    wait_time = between(5, 15)

    @task(1)
    def index(self):
        self.client.get("/")
