import psutil


cpu_usage = psutil.cpu_percent(interval=1)
print(f"CPU usage: {cpu_usage}%")