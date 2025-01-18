import requests 
from ..configs.constants import DISCORD_WEBHOOK_URL

def send_message(message: str):
    data = {
        "content": message
    }
    response = requests.post(DISCORD_WEBHOOK_URL, json=data)

    return response.status_code

def report_success(job, connection, result, *args, **kwargs):
    send_message(f"Job {'{' + job.id + '}'} Task completed successfully\nResult: {result}")

    return True
