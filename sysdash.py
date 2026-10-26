import psutil
import os

LABEL_WIDTH = 20
COLOUR_RED = "\033[31m"
COLOUR_YELLOW = "\033[33m"
COLOUR_GREEN = "\033[32m"
COLOUR_RESET = "\033[0m"

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
        print(f"{'CPU Usage:':<{LABEL_WIDTH}} {cpu_usage}%")
        print(f"{'CPU Temperature:':<{LABEL_WIDTH}} {cpu_temp:.1f}°C")
        print(f"{'RAM Usage:':<{LABEL_WIDTH}} {ram_used:.1f} / {ram_total:.1f} GB ({ram_percent:.1f}%)")
        print(f"{'Disk Usage:':<{LABEL_WIDTH}} {disk_used:.1f} / {disk_total:.1f} GB ({disk_percent:.1f}%)")
        print()
        print("PRESS CTRL+C TO QUIT")
except KeyboardInterrupt:
    print("\nStopped")