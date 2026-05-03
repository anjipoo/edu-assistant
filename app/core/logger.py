import datetime

def log_step(tag, message):
    time = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"[{time}] [{tag}] {message}")