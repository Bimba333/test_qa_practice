import asyncio
import aiohttp
import requests
import time

async def get_todo(session, todo_id):
    async with session.get(
        f"https://jsonplaceholder.typicode.com/todos/{todo_id}"
    ) as response:
        return await response.json()

async def get_todos(ids):
    async with aiohttp.ClientSession() as session:
        tasks = [get_todo(session, id) for id in ids]
        results = await asyncio.gather(*tasks)
        return results
    
def get_todos_sync(ids):
    results = []
    for id in ids:
        response = requests.get(f"https://jsonplaceholder.typicode.com/todos/{id}")
        results.append(response.json())
    return results

ids = [1, 2, 3, 4, 5]

start = time.time()
sync_result = get_todos_sync(ids)
sync_time = time.time() - start
print(f"Синхронно:   {len(sync_result)} записей за {sync_time:.2f}s")

start = time.time()
async_result = asyncio.run(get_todos(ids))
async_time = time.time() - start
print(f"Асинхронно:  {len(async_result)} записей за {async_time:.2f}s")

print(f"Быстрее в:   {sync_time/async_time:.1f}x")