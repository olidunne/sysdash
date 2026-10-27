# Notes

## 25 Oct
- Set up a virtual environment (.venv) and git
- cpu_percent() needs an interval or it returns 0.0 because it compares two readings over time
- virtual_memory() returns lots of values, using .percent after the brackets picks one the percentage value
- Learned functions: def, return, and calling with ()
- Learnt that tracebacks are to be read from the bottom up

## 26 Oct
- Pushed repo to github on PC
- Cloned repo from github to Mac and made a new .venv
- Added get_cpu_temp()
- Added get_disk_percent()
- Added "os" to allow the script to talk to the operating system
- Used a while loop so that the status of each component keeps updating
- Created new variables for each statistic at the start of the while loop to fix flashing when the monitor refreshes
- Placed the while loop within "try:" to make the process end cleanly when using Ctrl+C
- Added README.md
- Added a title and instructions to close within the program
- Added :<20 to each print line using the variable LABEL_WIDTH for equal spacing
- Added a function that converts bytes to Gigabytes
- Added ram and disk .used and .total
- Cleaned up functions and variables to make the code more readable and so that get_ram() and get_disk() only need to be called once per loop
- Added text colour variables for red, yellow, green, and reset.
- Added a colour coding system for warning and danger (get_colour) and applied it with cpu_temp
- Applied the colour coding to the other percentages
- Rearanged the print lines so that the percentage always comes first
- Set the percentage warning and danger values as constants
- Renamed bytes to num_bytes to avoid clashes with pythons default bytes() function
- Made a seperate branch to get started on the GUI
- Imported tkinter as tk
- Created a window
- Created labels for cpu usage and cpu temp and used .pack() to place them
- Started a .mainloop() to hand control to the window

# 27 Oct
- Merged main and gui
- Made a new branch called split-files to start reorganising the code into seperate files to prevent having to rewrite the code from sysdash.py into gui.py
- Added import stats on sysdash.py and placed stats. before the use of every function thats definition has been moved to stats.py
- Merged main and split-files
- Started gui-live branch
- Added interval option to get_cpu_usage
- Made cpu usage and temperature lables update live in gui
- Moved the definitions of disk and ram used, total, and percent into stats.py
- Made disk and ram labels update live in gui
- Switched pack() to grid()
- Added a version of get_colour to gui.py and made it function on the labels with fg=