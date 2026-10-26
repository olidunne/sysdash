import psutil
import os

LABEL_WIDTH = 20
COLOUR_RED = "\033[31m"
COLOUR_YELLOW = "\033[33m"
COLOUR_GREEN = "\033[32m"
COLOUR_RESET = "\033[0m"
CPU_USAGE_DANGER = 90
CPU_USAGE_WARNING = 70
CPU_TEMP_DANGER = 80
CPU_TEMP_WARNING = 70
RAM_DANGER = 90
RAM_WARNING = 75
DISK_DANGER = 90
DISK_WARNING = 80

def bytes_to_gb(bytes):
    return bytes / 1024**3

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

def get_colour(value, danger, warning):
    if value > danger:
        return COLOUR_RED
    elif value > warning:
        return COLOUR_YELLOW
    else:
        return COLOUR_GREEN

try:
    while True:
        cpu_usage = get_cpu_usage()
        cpu_temp = get_cpu_temp()
        ram = get_ram()
        disk = get_disk()
        ram_used = bytes_to_gb(ram.used)
        ram_total = bytes_to_gb(ram.total)
        ram_percent = (ram.percent)
        disk_used = bytes_to_gb(disk.used)
        disk_total = bytes_to_gb(disk.total)
        disk_percent = (disk.percent)
        os.system("clear")
        print("SYSDASH")
        print()
        print(f"{'CPU Usage:':<{LABEL_WIDTH}} {get_colour(cpu_usage, CPU_USAGE_DANGER, CPU_USAGE_WARNING)}{cpu_usage}%{COLOUR_RESET}")
        print(f"{'CPU Temperature:':<{LABEL_WIDTH}} {get_colour(cpu_temp, CPU_TEMP_DANGER, CPU_TEMP_WARNING)}{cpu_temp:.1f}°C{COLOUR_RESET}")
        print(f"{'RAM Usage:':<{LABEL_WIDTH}} {get_colour(ram_percent, RAM_DANGER, RAM_WARNING)}{ram_percent:.1f}%{COLOUR_RESET} ({ram_used:.1f} / {ram_total:.1f} GB)")
        print(f"{'Disk Usage:':<{LABEL_WIDTH}} {get_colour(disk_percent, DISK_DANGER, DISK_WARNING)}{disk_percent:.1f}%{COLOUR_RESET} ({disk_used:.1f} / {disk_total:.1f} GB)")
        print()
        print("PRESS CTRL+C TO QUIT")
except KeyboardInterrupt:
    print("\nStopped")