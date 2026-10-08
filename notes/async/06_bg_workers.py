import asyncio
import threading
import time

def background_worker():
    while True:
        time.sleep(1)
        print(f"Logging the system health 🕰️")

async def fetch_orders():
    await asyncio.sleep(3)
    print("🎁 order fetched")

threading.Thread(target=background_worker, daemon = True).start()

asyncio.run(fetch_orders())

# project -  can build something like an interesting chai delivery SaaS platform where asyncio takes or talks to the third party like Google Maps or Razorpay, while there is a background multiprocessing. Probably simulate a machine learning model, which predicts the T demand. Again all fictitious.

# Throw up some random data after some time and you can also use threads to keep the UIs and the logs responsive. Maybe log every single time that. Okay, this system has been active for this second and this second. So try to design these kinds of things.
