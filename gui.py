import stats
import tkinter as tk

window = tk.Tk()
window.title("sysdash")
window.geometry("300x150")

label_cpu_usage_name = tk.Label(window, text="CPU Usage:")
label_cpu_temp_name = tk.Label(window, text="CPU Temperature:")
label_ram_usage_name = tk.Label(window, text="RAM Usage:")
label_disk_usage_name = tk.Label(window, text="Disk Usage:")

label_cpu_usage_name.grid(row=0, column=0)
label_cpu_temp_name.grid(row=1, column=0)
label_ram_usage_name.grid(row=2, column=0)
label_disk_usage_name.grid(row=3, column=0)

label_cpu_usage = tk.Label(window, text="--")
label_cpu_temp = tk.Label(window, text="--")
label_ram_usage = tk.Label(window, text="--")
label_disk_usage = tk.Label(window, text="--")

label_cpu_usage.grid(row=0, column=1)
label_cpu_temp.grid(row=1, column=1)
label_ram_usage.grid(row=2, column=1)
label_disk_usage.grid(row=3, column=1)

def update():
    cpu_usage = stats.get_cpu_usage(interval=None)
    label_cpu_usage.config(text=f"{cpu_usage}%")
    cpu_temp = stats.get_cpu_temp()
    label_cpu_temp.config(text=f"{cpu_temp:.1f}°C")
    ram_used, ram_total, ram_percent = stats.get_ram_stats()
    label_ram_usage.config(text=f"{ram_percent}% ({ram_used:.1f} / {ram_total:.1f} GB)")
    disk_used, disk_total, disk_percent = stats.get_disk_stats()
    label_disk_usage.config(text=f"{disk_percent}% ({disk_used:.1f} / {disk_total:.1f} GB)")
    window.after(1000, update)

update()

window.mainloop()