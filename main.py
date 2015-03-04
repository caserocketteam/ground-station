import Tkinter as tk
import time
import getData
import callbacks
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

gps = tk.Button(root, text="Connect GPS", command=callbacks.gps_callback).grid(row=0, column=3)

alive = True

def run():
  while True:
    print getData.read()
    alt_val.set(getData.get_alt())
    rot_val.set(getData.get_rot())
    acc_val.set(getData.get_acc())
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
