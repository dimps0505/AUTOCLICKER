import keyboard
import time
import pyautogui
import threading
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
import sys

pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False

running = False
delay = 0

def auto_clicker():
    global running, delay
    next_time = time.perf_counter()

    while running:
        pyautogui.click()

        next_time += delay
        sleep_time = next_time - time.perf_counter()

        if sleep_time > 0:
            time.sleep(sleep_time)

def toggle():
    global running
    running = not running

    if running:
        threading.Thread(target=auto_clicker, daemon=True).start()

root = tk.Tk()
root.withdraw()

cps = simpledialog.askinteger(
    "CPS",
    "What CPS would you like?",
    parent=root,
    minvalue=1,
    maxvalue=250
)

if cps is None:
    sys.exit()

delay = 1 / cps

root = tk.Tk()
root.withdraw()

keybind = simpledialog.askstring(
    "Keybind",
    "What Keybind would you like? (Recommended f1 to f12)",
    parent=root,
)

messagebox.showinfo(
    "Auto Clicker",
    f"Press {keybind} to toggle clicking.\nPress ESC to exit."
)

root.destroy()

keyboard.add_hotkey(keybind, toggle)
keyboard.wait("esc")