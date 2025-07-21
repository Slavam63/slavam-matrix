import requests

def notify_result():
    endpoint = "https://api.notification.service/send"
    payload = {
        "title": "Matrix Update",
        "message": "Матрица завершила цикл: отчёт создан и адаптирован.",
        "channel": "slavam-alert"
    }
    response = requests.post(endpoint, json=payload)
    response.raise_for_status()

if __name__ == "__main__":
    notify_result()
