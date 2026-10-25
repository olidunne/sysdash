import psutil

def get_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    return cpu_usage

def get_ram():
    ram_usage = psutil.virtual_memory().percent
    return ram_usage

print(f"CPU usage: {get_cpu()}%")
print(f"RAM usage: {get_ram()}%")