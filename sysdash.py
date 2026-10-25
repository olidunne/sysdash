import psutil

def get_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    return cpu_usage

print(f"CPU usage: {get_cpu()}%")