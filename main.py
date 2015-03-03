import Tkinter as tk
import time
import getData
from threading import Thread

root = tk.Tk()
root.wm_title("CRT Telemetry")
root.geometry('{}x{}'.format(600, 400))

alt_val = tk.StringVar()
rot_val = tk.StringVar()
acc_val = tk.StringVar()

alt = tk.Label(root, textvariable=alt_val).pack
rot = tk.Label(root, textvariable=rot_val).pack
acc = tk.Label(root, textvariable=acc_val).pack

def run():
  print getData.read()
  alt_val.set("0.00 m")
  rot_val.set("0.00 d/s")
  acc_val.set("0.00 m/s")
  time.sleep(1)

def data():
  while True:
    run()

thread = Thread(target=data)
thread.start()
root.mainloop()
