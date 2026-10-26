import psutil

def get_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    return cpu_usage

def get_ram():
    ram_usage = psutil.virtual_memory().percent
    return ram_usage

def get_cpu_temp():
    cpu_temp = psutil.sensors_temperatures()['k10temp'][0].current
    return cpu_temp

print(f"CPU usage: {get_cpu()}%")
print(f"RAM usage: {get_ram()}%")
print(f"CPU Temperature: {get_cpu_temp():.1f}°C")