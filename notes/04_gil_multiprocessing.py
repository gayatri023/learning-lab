from multiprocessing import Process
import time

def crunch_number():
    print(f"Started the count process")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"Ended the count process...")

if __name__ == "__main__":
    start = time.time()

    p1 = Process(target=crunch_number)
    p2 = Process(target=crunch_number)

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    end = time.time()

    print(f"Total time with multi-processing is {end-start:.2f} seconds")


# point to be note - it is faster then other but we are over riding mutex - the security feature - so we have to be careful for it but we need to know when GIL impelementation is good and hte lock is good and wehn to actually avoid and bypass it and speed up the process

