import threading
import time

start_time = time.time()
def my_sleep_method(secs):
    time.sleep(secs)
    name1 = threading.currentThread().getName()
    print (f"{name1} slept for {secs} seconds.", end="\n")

threads=[]
for num in range(10):
    process = threading.Thread(name=f"thread_{num}", target=my_sleep_method, args=[4])
    process.start()
    threads.append(process)

for process in threads:
    process.join()

print("--- %s seconds ---" % (time.time() - start_time))