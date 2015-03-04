import Tkinter as tk
import time
import getData
import sendData
from threading import Thread

root = tk.Tk()
root.wm_title("CRT Telemetry")
root.geometry('{}x{}'.format(600, 400))

alt_val = tk.StringVar()
rot_val = tk.StringVar()
acc_val = tk.StringVar()

alt_label = tk.Label(root, text="Altitude:    ").grid(row=0, column=0)
rot_label = tk.Label(root, text="Rotation:    ").grid(row=1, column=0)
acc_label = tk.Label(root, text="Acceleration:").grid(row=2, column=0)

alt = tk.Label(root, textvariable=alt_val).grid(row=0, column=1)
rot = tk.Label(root, textvariable=rot_val).grid(row=1, column=1)
acc = tk.Label(root, textvariable=acc_val).grid(row=2, column=1)

def gps_callback():
  sendData.start_gps()

gps = tk.Button(root, text="Connect GPS", command=gps_callback).grid(row=0, column=3)

def gps_callback():
  sendData.start_gps()

alive = True

def run():
  while True:
    print getData.read()
    alt_val.set("0.00 m")
    rot_val.set("0.00 d/s")
    acc_val.set("0.00 m/s")
    time.sleep(1)
    if alive == False:
      raise Exception("Window Closed...")

thread = Thread(target=run)

def handler():
  alive = False
  root.quit()

root.protocol("WM_DELETE_WINDOW", handler)

thread.start()
root.mainloop()
