from locust import HttpUser, task, wait_time

class AIRagUser(HttpUser):
    wait_time = wait_time.between(1, 5)

    @task
    def ask_question(self):
        self.client.post("/query", json={
            "user_input": "Explain quantum computing in 3 sentences.",
            "session_id": "test-user-1"
        })