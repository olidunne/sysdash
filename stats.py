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

def get_cpu_usage(interval=1):
    cpu_usage = psutil.cpu_percent(interval=interval)
    return cpu_usage

def get_cpu_temp():
    cpu_temp = psutil.sensors_temperatures()['k10temp'][0].current
    return cpu_temp

def get_ram_stats():
    ram = psutil.virtual_memory()
    ram_used = bytes_to_gb(ram.used)
    ram_total = bytes_to_gb(ram.total)
    ram_percent = ram.percent
    return ram_used, ram_total, ram_percent

def get_disk_stats():
    disk = psutil.disk_usage("/")
    disk_used = bytes_to_gb(disk.used)
    disk_total = bytes_to_gb(disk.total)
    disk_percent = disk.percent
    return disk_used, disk_total, disk_percent