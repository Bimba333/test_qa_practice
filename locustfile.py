from locust import HttpUser, task, between

class LogisticsUser(HttpUser):
    host = "https://jsonplaceholder.typicode.com"
    wait_time = between(1, 3)

    @task(3)
    def view_orders(self):
        self.client.get("/todos")

    @task(2)
    def view_single_order(self):
        self.client.get("/todos/1")

    @task(1)
    def create_order(self):
        self.client.post("/todos", json={
            "title": "Новый заказ",
            "completed": False,
            "userId": 1
        })