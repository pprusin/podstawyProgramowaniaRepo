import asyncio

async def print_numbers():
    for i in range(1, 8):
        print(i)
        await asyncio.sleep(1)

asyncio.run(print_numbers())
