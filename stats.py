import psutil

CPU_USAGE_DANGER = 90
CPU_USAGE_WARNING = 70
CPU_TEMP_DANGER = 80
CPU_TEMP_WARNING = 70
RAM_DANGER = 90
RAM_WARNING = 75
DISK_DANGER = 90
DISK_WARNING = 80

def bytes_to_gb(num_bytes):
    return num_bytes / 1024**3

def get_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    return cpu_usage

def get_cpu_temp():
    cpu_temp = psutil.sensors_temperatures()['k10temp'][0].current
    return cpu_temp

def get_ram():
    ram_usage = psutil.virtual_memory()
    return ram_usage

def get_disk():
    disk_used = psutil.disk_usage("/")
    return disk_used