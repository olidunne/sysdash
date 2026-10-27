import stats
import os

LABEL_WIDTH = 20

COLOUR_RED = "\033[31m"
COLOUR_YELLOW = "\033[33m"
COLOUR_GREEN = "\033[32m"
COLOUR_RESET = "\033[0m"


def get_colour(value, danger, warning):
    if value > danger:
        return COLOUR_RED
    elif value > warning:
        return COLOUR_YELLOW
    else:
        return COLOUR_GREEN

try:
    while True:
        cpu_usage = stats.get_cpu_usage()
        cpu_temp = stats.get_cpu_temp()
        ram_used, ram_total, ram_percent = stats.get_ram_stats()
        disk_used, disk_total, disk_percent = stats.get_disk_stats()
        os.system("clear")
        print("SYSDASH")
        print()
        print(f"{'CPU Usage:':<{LABEL_WIDTH}} {get_colour(cpu_usage, stats.CPU_USAGE_DANGER, stats.CPU_USAGE_WARNING)}{cpu_usage}%{COLOUR_RESET}")
        print(f"{'CPU Temperature:':<{LABEL_WIDTH}} {get_colour(cpu_temp, stats.CPU_TEMP_DANGER, stats.CPU_TEMP_WARNING)}{cpu_temp:.1f}°C{COLOUR_RESET}")
        print(f"{'RAM Usage:':<{LABEL_WIDTH}} {get_colour(ram_percent, stats.RAM_DANGER, stats.RAM_WARNING)}{ram_percent:.1f}%{COLOUR_RESET} ({ram_used:.1f} / {ram_total:.1f} GB)")
        print(f"{'Disk Usage:':<{LABEL_WIDTH}} {get_colour(disk_percent, stats.DISK_DANGER, stats.DISK_WARNING)}{disk_percent:.1f}%{COLOUR_RESET} ({disk_used:.1f} / {disk_total:.1f} GB)")
        print()
        print("PRESS CTRL+C TO QUIT")
except KeyboardInterrupt:
    print("\nStopped")