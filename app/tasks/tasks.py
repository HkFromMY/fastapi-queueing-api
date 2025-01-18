import time

def background_task(seconds: int):
    time.sleep(seconds)
    return f"Task completed after {seconds} seconds."
