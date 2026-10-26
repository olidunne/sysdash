import psutil
import os

LABEL_WIDTH = 20

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
        ram_used = f"{bytes_to_gb(ram.used):.1f}"
        ram_total = f"{bytes_to_gb(ram.total):.1f}"
        ram_percent = f"{(ram.percent):.1f}"
        disk_used = f"{bytes_to_gb(disk.used):.2f}"
        disk_total = f"{bytes_to_gb(disk.total):.2f}"
        disk_percent = f"{(disk.percent):.1f}"

        os.system("clear")
        print("SYSDASH")
        print()
        print(f"{'CPU Usage:':<{LABEL_WIDTH}} {cpu_usage}%")
        print(f"{'CPU Temperature:':<{LABEL_WIDTH}} {cpu_temp:.1f}°C")
        print(f"{'RAM Usage:':<{LABEL_WIDTH}} {ram_used} / {ram_total} GB ({ram_percent}%)")
        print(f"{'Disk Usage:':<{LABEL_WIDTH}} {disk_used} / {disk_total} GB ({disk_percent}%)")
        print()
        print("PRESS CTRL+C TO QUIT")
except KeyboardInterrupt:
    print("\nStopped")