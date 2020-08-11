import random
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(0.5, 1)
    my_darksky = "https://api.darksky.net/forecast/0b456bc491291527b0568143cd84085b/50.401699,30.252512?units=si"

    @task
    def index_page(self):
        self.client.get("/forecast/0b456bc491291527b0568143cd84085b/50.401699,30.252512?units=si")
