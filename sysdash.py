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

def get_disk_percent():
    disk_percent_used = psutil.disk_usage("/").percent
    return disk_percent_used

print(f"CPU Usage: {get_cpu()}%")
print(f"RAM Usage: {get_ram()}%")
print(f"CPU Temperature: {get_cpu_temp():.1f}°C")
print(f"Disk % Used: {get_disk_percent():.1f}%")