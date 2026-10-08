import asyncio
import aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:  # session to get request and post request etc
        print(f"Fetched {url} with status {response.status}")

async def main():
    urls = ["https://httpbin.org/delay/2"] * 3
    async with aiohttp.ClientSession() as session:   
        tasks = [fetch_url(session, url) for url in urls]
        #tasks = [t1, t2, t3]  --- instead of t1, t2, t3 in *tasks as it unpack
        await asyncio.gather(*tasks)   

asyncio.run(main())
# blocking and non blocking task
