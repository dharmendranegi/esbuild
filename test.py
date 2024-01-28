from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("https://dslsi9j2pb.execute-api.ap-south-1.amazonaws.com/dev/hello")