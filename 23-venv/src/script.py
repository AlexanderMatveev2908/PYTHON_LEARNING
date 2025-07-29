import asyncio
from typing import Dict
import httpx
import os
from dotenv import load_dotenv


load_dotenv()

api = httpx.AsyncClient(base_url="https://jsonplaceholder.typicode.com")


async def get_posts() -> list[Dict]:
    res = await api.get("/posts")
    res = res.json()
    return res


async def get_users() -> list[Dict]:
    res = await api.get("/users")
    res = res.json()
    return res


# posts = asyncio.run(get_posts())
# for i in range(10):
#     print(posts[i])


async def main() -> None:
    users, posts = await asyncio.gather(get_users(), get_posts())

    for data in [users, posts]:
        for i in range(5):
            print(data[i])


# asyncio.run(main())

print(os.getenv("SECRET"))
