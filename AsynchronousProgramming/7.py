import asyncio

async def long_running_task():
    print("Task started...")
    await asyncio.sleep(10)  
    print("Task completed.")

async def main():
    try:
        await asyncio.wait_for(long_running_task(), timeout=5) 
    except asyncio.TimeoutError:
        print("The task timed out.")

asyncio.run(main())
