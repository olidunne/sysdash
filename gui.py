import stats
import tkinter as tk

window = tk.Tk()
window.title("sysdash")
window.geometry("300x150")

label_cpu_usage = tk.Label(window, text="CPU Usage: --")
label_cpu_temp = tk.Label(window, text="CPU Temperature: --")

label_cpu_usage.pack()
label_cpu_temp.pack()

def update():
    cpu_usage = stats.get_cpu_usage(interval=None)
    label_cpu_usage.config(text=f"CPU Usage: {cpu_usage}%")
    cpu_temp = stats.get_cpu_temp()
    label_cpu_temp.config(text=f"CPU Temperature: {cpu_temp:.1f}°C")
    window.after(1000, update)

update()

window.mainloop()