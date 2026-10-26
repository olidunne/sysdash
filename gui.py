import tkinter as tk

window = tk.Tk()
window.title("sysdash")
window.geometry("300x150")

label_cpu_usage = tk.Label(window, text="CPU Usage: --")
label_cpu_temp = tk.Label(window, text="CPU Temperature: --")

label_cpu_usage.pack()
label_cpu_temp.pack()
window.mainloop()