import asyncio

async def display_name_1():
    await asyncio.sleep(1)
    print("Function 1")

async def display_name_2():
    await asyncio.sleep(2)
    print("Function 2")

async def display_name_3():
    await asyncio.sleep(3)
    print("Function 3")

async def main():
    await asyncio.gather(display_name_1(), display_name_2(), display_name_3())

asyncio.run(main())
