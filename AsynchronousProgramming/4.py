import asyncio
import aiohttp

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text()
            print(f"Data from {url[:30]}: {data[:100]}...")  # Print first 100 characters for brevity

async def main():
    url1 = "https://jsonplaceholder.typicode.com/posts/1"
    url2 = "https://jsonplaceholder.typicode.com/posts/2"
    await asyncio.gather(fetch_data(url1), fetch_data(url2))

asyncio.run(main())
