import asyncio
import random

async def producer(queue, producer_id):
    for i in range(5):
        item = f"item_{i}_from_producer_{producer_id}"
        await asyncio.sleep(random.uniform(0.1, 1.0))
        await queue.put(item)
        print(f"Producer {producer_id} produced {item}")

async def consumer(queue):
    while True:
        item = await queue.get()
        if item is None:
            break
        await asyncio.sleep(random.uniform(0.1, 0.5))
        print(f"Consumer consumed {item}")
        queue.task_done()

async def main():
    queue = asyncio.Queue()
    producers = [producer(queue, i) for i in range(3)]
    consumer_task = asyncio.create_task(consumer(queue))

    await asyncio.gather(*producers)
    await queue.put(None)  # Sentinel to stop the consumer
    await consumer_task

asyncio.run(main())
