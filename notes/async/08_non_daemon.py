import threading 
import time

def monitor_tea_temp():
    while True:
        print(f"Monitoring tea temperature...")
        time.sleep(2)

t=threading.Thread(target=monitor_tea_temp)
t.start()

print("Main program done")
# profiling task == code - python -m cProfile -S TIME 08_non_daemon.py - tell what is happening and what is going on
