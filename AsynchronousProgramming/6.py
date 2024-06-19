import asyncio

async def time_consuming_task():
    print("Task started...")
    try:
        for i in range(10):
            await asyncio.sleep(1)
            print(f"Working... {i+1}")
    except asyncio.CancelledError:
        print("Task was cancelled!")
        raise
    else:
        print("Task completed successfully.")

async def main():
    task = asyncio.create_task(time_consuming_task())
    await asyncio.sleep(5)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("Main caught the cancellation.")

asyncio.run(main())
