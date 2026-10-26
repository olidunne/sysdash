import psutil
import os

LABEL_WIDTH = 20

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

try:
    while True:
        cpu = get_cpu()
        ram = get_ram()
        cpu_temp = get_cpu_temp()
        disk_percent = get_disk_percent()
        os.system("clear")
        print("SYSDASH")
        print()
        print(f"{'CPU Usage:':<{LABEL_WIDTH}} {cpu}%")
        print(f"{'RAM Usage:':<{LABEL_WIDTH}} {ram}%")
        print(f"{'CPU Temperature:':<{LABEL_WIDTH}} {cpu_temp:.1f}°C")
        print(f"{'Disk Usage:':<{LABEL_WIDTH}} {disk_percent:.1f}%")
        print()
        print("PRESS CTRL+C TO QUIT")
except KeyboardInterrupt:
    print("\nStopped")