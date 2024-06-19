import asyncio
import time

async def task(name, delay):
    await asyncio.sleep(delay)
    print(f"Task {name} completed after {delay} seconds")

async def main():
    tasks = [
        task("A", 2),
        task("B", 3),
        task("C", 1)
    ]
    start_time = time.time()
    await asyncio.gather(*tasks)
    end_time = time.time()
    print(f"Total time taken: {end_time - start_time:.2f} seconds")

asyncio.run(main())
